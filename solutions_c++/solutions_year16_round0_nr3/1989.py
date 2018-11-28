#include <iostream>
#include <string>
#include <fstream>
#include <set>
#include <cmath>
#include <map>
#include <vector>

using namespace std;

bool TOOLONGMODE = false;

map<long long, set<long long> > composites;
vector<long long> primes;

void Primes(long long num) {
    cout << "Primes up to : " << num <<endl;
    long long sqrt_num = sqrt(num);
    for (long long j = 2; j <= sqrt_num; ++j) {
        if (composites.count(j) > 0) {
            continue;
        }
        primes.push_back(j);
        for (long long i = j*2; i <= num; i+=j) {
            composites[i].insert(j);
        }
    }
}

void PrintPrimes() {
    for (pair<long , set<long long> > p : composites) {
        cout << p.first << "\t";
        for (long long i : p.second) {
            cout << i << ",";
        }
        cout<<endl;
    }

    for (long long p : primes) {
        cout << p << " ";
    }
    cout<<endl;
}

bool CheckOnly01s(int num, int base) {
    while (num != 0) {
        if (num % base > 1) {
            return false;
        }
        num /= base;
    }
    return true;
}

bool CheckJamCoin(long long num, int base, int length) {
    if (num % 2 == 0) return false;
    if (pow(base, length - 1) > num) return false;

    return CheckOnly01s(num, base);
}


long long ComputeNum(int base, const vector<int>& arr, int prime) {
    long long num = 0;

    for (int a : arr) {
        if (num > prime) {
            num %= prime;
        }
        num *= base;
        num += base * a;

    }
    num /= base;
    return num;
}

bool Increment(vector<int>& arr) {
    if (arr.size() < 3) {
        return false;
    }

    int i = arr.size() - 2;
    for (; i >= 1; --i) {
        if (arr[i] == 0)  {
            arr[i] = 1;
            return true;
        }
        arr[i] = 0;
    }
    return i != 0;
}

map<pair<int, long long>, bool> base_to_correct;

bool IsPrime(const vector<int>& arr, long long & div, int base, int length) {
    /*if (composites.count(num) == 0) {
        return true;
    }
    return false;*/
    for (int d = 0; d < primes.size(); ++d) {
        long long n = ComputeNum(base, arr, primes[d]);
        if (n % primes[d] == 0) {
            div = primes[d];
            return false;
        }
    }
    return true;
}

bool IsJamCoin(const vector<int>& arr, vector<long long>& divs, int length) {
        for (int b = 2; b <= 10; b ++) {
            long long div;
            if (IsPrime(arr, div, b, length)) {
                //cerr << b << " " << flush;
                return false;
            }
            divs.push_back(div);
        }
        return true;
}

                                           // bits,                 divisors
void ReturnJamCoins(int length, int count, vector<pair<vector<int>, vector<long long> > >& jamcoins) {
    vector<int> arr;
    for (int i = 0; i < length; ++i) {
        arr.push_back(0);
    }
    arr[arr.size()-1] = 1;
    arr[0] = TOOLONGMODE ? 0 : 1;

    do {
        vector<long long> divs;
        if (IsJamCoin(arr, divs, length)) {
            jamcoins.push_back(pair< vector<int> , vector<long long> > (arr, divs ));
            cout << jamcoins.size() << " " << flush;
        }
        if (jamcoins.size() >= count) {
            break;
        }

    } while(Increment(arr));
}



int main(int argc, char* argv[]) {
    /*cout << CheckFirstDigit(10, 32, 7)<<endl;
    return 0;*/
    if (argc != 2) {
        cerr << "Give file name\n";
        return -1;
    }
    string fn = argv[1];
    ifstream input;
    input.open(fn.c_str());
    fn = fn.append(".out.txt");
    ofstream output;
    output.open(fn);

    int num_of_problems, count, length;
    input >> num_of_problems >> length >> count;


    Primes(pow(2,length / 2) );
    //PrintPrimes();
    cout <<"Primes done\n";

    output << "Case #1:"<< endl;
    vector< pair <  vector<int>,
                    vector<long long >
                 >  > jamcoins_with_divs;

    ReturnJamCoins(length, count, jamcoins_with_divs);
    for (auto& jc : jamcoins_with_divs) {
    	jc.first[0] = 1;
        for (int i : jc.first) {
            output<<i;
        }

        for (int b = 2; b<=10; b ++ /* b+= 2*/) {
           // long long num = ComputeNum(b, jc.first);
           // output <<" " << *(composites[num].begin());

           // output <<" " << jc.second[b/2 - 1];
            output <<" " << jc.second[b - 2];
           /* if (b != 10) {
            	output <<" " <<2;
            }*/

        }
        output<<endl;
    }

    output.close();
    input.close();
    return 0;
}