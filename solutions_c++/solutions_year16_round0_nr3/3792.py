#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <fstream>
#include <set>
#include <cmath>
#include <unordered_set>


struct Jamcoin {
    unsigned long long num;
    std::vector<unsigned long long> divisors;
};

struct PrimeCache {
    std::vector<unsigned long long> primes;
    std::unordered_set<unsigned long long> primesSet;
};


void
loadSomePrimes(PrimeCache& cache)
{
    std::ifstream f("primes_processed.txt", std::ios::in);
    unsigned int p;
    while (f >> p) {
        cache.primes.push_back(p);
        cache.primesSet.insert(p);
    }
}

unsigned long long 
getRep(unsigned long long num, int sourceBase, int destBase = 10)
{
    if (sourceBase == destBase) {
        return num;
    }
    int power=0;
    unsigned long long result=0;
    unsigned long long powAccum = 1;
    while(num > 0) {    
        result += (num % destBase) * pow(sourceBase,power++);
        num /= destBase;
    }
    return result;
}



bool
isPrime(unsigned long long n, PrimeCache& pc, unsigned long long& someDiv)
{
    if (pc.primesSet.find(n) != pc.primesSet.end()) {
        return true;
    }
    
    unsigned long long upperBound = std::sqrt(n);
    for (unsigned int i = 0; i < pc.primes.size(); ++i) {
        unsigned long long prime = pc.primes[i];
        if (prime > upperBound) {
            break;
        }
        // check if we can divide by the prime
        if (n % prime == 0) {
            someDiv = prime;
            return false;
        }
    }
    
    // now we go brute force
    unsigned long long divisor = pc.primes.back() + 2;
    while (divisor <= upperBound) {
        if (n % divisor == 0) {
            someDiv = divisor;
            return false;
        }
        divisor += 2;
    }
    
    // is prime! :( add it to the cache
    pc.primesSet.insert(n);
    return true;
}


void
printCase(int caseNum, std::vector<Jamcoin>& jcs, int N)
{
    static std::string str;
    str.resize(N);
    std::cout << "Case #" << caseNum << ":\n";
    for (const Jamcoin& jc : jcs) {
        /*for (int dig = N-1; dig >= 0; dig--) {
            str[dig] = (jc.num & (1 << dig) == 0) ? '0' : '1';
        }
        std::stringstream ss;
        ss << getRep(jc.num, 10, 2);
        ss >> str;
        std::cout << str;*/
        std::cout << jc.num;
        for (int i = 0; i < jc.divisors.size(); ++i) {
            std::cout << " " << jc.divisors[i];
        }
        std::cout << "\n";
    }
}

void
calculate(int J, int N, std::vector<Jamcoin>& result, PrimeCache& pc)
{
    static std::vector<int> bases{2,3,4,5,6,7,8,9,10};
    std::vector<unsigned long long> reps;
    reps.resize(bases.size());
    result.reserve(J);
    
    // we need to generate at least J numbers of N digits.
    // to do this what we will do is as follows
    unsigned long long base = (1 << (N-1)) | (1);
    unsigned long long totalSubNums = 1 << (N-2);
    //std::cout << "total sub nums: " << totalSubNums << "\n";
    for (unsigned long long subNum = 0; subNum < totalSubNums; ++subNum) {
        unsigned long long candidate = base | (subNum << 1);
        candidate = getRep(candidate, 10, 2);
        //std::cout << " current num: " << candidate << "\n";
        
        // calculate the number in the different bases
        bool isGoodCandidate = true;
        for (int i = 0; i < bases.size(); ++i) {
            unsigned long long rep = getRep(candidate, bases[i]);
            //std::cout << "\trep: " << rep << " for base: " << bases[i] << "\n";
            unsigned long long divisor = 0;
            if (isPrime(rep, pc, divisor)) {
            //std::cout << "IT ISSSS prime\n";
                isGoodCandidate = false;
                break;
            }
            //std::cout << "is not prime\n";
            reps[i] = divisor;
        }
        if (isGoodCandidate) {
            Jamcoin jc;
            jc.num = candidate;
            jc.divisors = reps;
            result.push_back(jc);
        }
        
        if (result.size() == J) {
            return;
        }
    }
    
}



int main(void)
{
    int T;
    std::cin >> T;
    PrimeCache pc;
    loadSomePrimes(pc);
    for (int i = 0; i < T; ++i) {
        int N, J;
        std::cin >> N >> J;
        std::vector<Jamcoin> result;
        calculate(J, N, result, pc);
        printCase(i + 1, result, N);
        
    }

    return 0;
}
