#include <iostream>
#include <stack>
#include <vector>
#include <cmath>

using namespace std;

unsigned long long MAX;
vector<int> primes;

unsigned long long baseChange(unsigned long long N, int M, int P) {
    stack<int> stk;
    long long NbaseM = 0;
    for(; N != 0; N /= P) {
        stk.push(N%P);
    }
    for(; !stk.empty(); stk.pop()) {
        NbaseM *= M;
        NbaseM += stk.top();
    }
    return NbaseM;
}

void genPrimes() {
    bool coprime = true;
    primes.push_back(2);
    for(int i = 3; i <= sqrt(baseChange(MAX, 10, 2)); i+=2) {
        for(int j = 0; i <= sqrt(primes[j]); j++) {
            if(i % primes[j] == 0) {
                coprime = false;
                continue;
            }
        }
        if(coprime)
            primes.push_back(i);
        if(primes.size() > 10000)
            break;
    }
}

long long checkPrime(unsigned long long N) {
    int size = primes.size();
    for(int i = 0; primes[i] <= sqrt(N) && i < size; i++)
        if(N % primes[i] == 0)
            return primes[i];
    return 0;
}

int *checkJamCoin(unsigned long long y[9]) {
    int *divisors = new int[9];
    int *dummy = new int[1];
    dummy[0] = 0;
    int divisor;
    for(int i = 0; i < 9; i++) {
        divisor = checkPrime(y[i]);
        if(divisor == 0)
            return dummy;
        else
            divisors[i] = divisor;
    }
    return divisors;
}

int main()
{
    int T, N, J, count = 0, *divisors;
    unsigned long long y[9];
    cin >> T;
    for(int i = 1; i <= T; i++) {
        cout << "Case #" << i << ": " << endl;
        cin >> N >> J;
        MAX = pow(2, N);
        genPrimes();
        for(int i = MAX/2 + 1; count < J; i+= 2) {
            y[8] = baseChange(i, 10, 2);
            for(int j = 2; j < 10; j++) {
                y[j - 2] = baseChange(y[8], j, 10);
            }
            divisors = checkJamCoin(y);
            if(divisors[0] != 0) {
                cout << y[8] << ' ';
                for(int j = 0; j < 9; j++)
                    cout << divisors[j] << ' ';
                cout << endl;
                count++;
            }
        }
    }
}
