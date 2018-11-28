#include<iostream>
#include<fstream>
#include<sstream>
#include<array>
#include<algorithm>
#include<vector>
#include<queue>

#include<gmp.h>
#include<gmpxx.h>

typedef unsigned long long ull;


struct input {
    uint64_t N, J;
};

struct JC {
  std::string S;
  std::array<uint32_t, 9> D;
};

struct output {
    std::vector<JC> JCs;
};

input parse(std::string line) {
    std::stringstream ss;
    ss << line;
    input I;
    ss >> I.N >> I.J;
    return I;
}


// Interface to the GMP random number functions.
gmp_randclass rng(gmp_randinit_default);

// Returns a divisor of N using Pollard's rho method.
mpz_class getDivisor(const mpz_class &N)
{
    mpz_class c = rng.get_z_range(N);
    mpz_class x = rng.get_z_range(N);
    mpz_class y = x;
    mpz_class d = 1;
    mpz_class z;

    while (d == 1) {
        x = (x*x + c) % N;
        y = (y*y + c) % N;
        y = (y*y + c) % N;
        z = x - y;
        mpz_gcd(d.get_mpz_t(), z.get_mpz_t(), N.get_mpz_t());
    }

    return d;
}




// Adds the prime factors of N to the given vector.
void factor(const mpz_class &N, std::vector<mpz_class> &factors)
{
    std::queue<mpz_class> to_factor;
    to_factor.push(N);

    while (!to_factor.empty()) {
        mpz_class n = to_factor.front();
        to_factor.pop();
        if (n == 1) {
            continue; // Trivial factor.
        } else if (mpz_probab_prime_p(n.get_mpz_t(), 5)) {
            // n is a prime.
            factors.push_back(n);
        } else {
            // n is a composite, so push its factors on the queue.
            mpz_class d = getDivisor(n);
            to_factor.push(d);
            to_factor.push(n/d);
        }
    }
}







int64_t factor(mpz_class N) {
    if (N%2 == 0) {
        return 2;
    }
    if (mpz_probab_prime_p(N.get_mpz_t(), 50)) {
        return -1;
    }
    std::vector<mpz_class> factors;
    factor(N, factors);
    std::sort(factors.begin(), factors.end());
    if (!factors[0].fits_ulong_p()) {
        std::cout << "ARGS\n";
        exit(1);
    }
    return factors[0].get_ui();
}

bool test(uint64_t M, uint32_t len) {
    uint64_t A = M*2+1 + (1ULL << (len -1));
    mpz_class AM = A;
    std::string S = AM.get_str(2);
    for (int i=2; i<=10; i++) {
        mpz_class B(S, i);
        if (factor(B) == -1)
            return false;
    }
    return true;
}

JC getJC(uint64_t M, uint32_t len) {
    JC J;
    uint64_t A = M*2+1 + (1ULL << (len -1));
    mpz_class AM = A;
    std::string S = AM.get_str(2);
    J.S = S;
    for (int i=2; i<=10; i++) {
        mpz_class B(S, i);
        J.D[i-2] = factor(B);
    }
    return J;
}

output solve(input I){
    output O;
    
    for (uint64_t m = 0; m < (1ULL << (I.N-2)); m++) {
        if (test(m, I.N)) {
            O.JCs.push_back(getJC(m, I.N));
            std::cerr << O.JCs.size() << " " << O.JCs.back().S << "\n";
        }
        if (O.JCs.size() == I.J) {
            break;
        }
    }
    
    return O;
}

void print(output O, uint32_t line) {
    std::cout << "Case #" << line << ": ";
    std::cout << "\n";
    for (auto J : O.JCs) {
        std::cout << J.S;
        for (auto d : J.D)
            std::cout << " " << d;
        std::cout << "\n";
    }
    std::cout << "\n";
}

int main(int argc, char* argv[]) {
    std::vector<std::string> args(argv, argv+argc);
    if (args.size() != 2)
        return 1;
    std::ifstream ifs(args[1]);
    std::string line;
    uint32_t lineNr = 0;
    while (true) {
        std::getline(ifs, line);
        if (!ifs)
            break;
        if (lineNr == 0) {
            lineNr = 1;
            continue;
        }
        input I = parse(line);
        output O = solve(I);
        print(O, lineNr++);
    }
}