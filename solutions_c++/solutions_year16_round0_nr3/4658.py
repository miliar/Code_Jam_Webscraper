#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

const long long MAX_PR = 1 << 25;
bool isprime[MAX_PR];
void eratosthenes_sieve(int LIMIT) {
    memset(isprime, 1, sizeof(isprime));
    isprime[0]=isprime[1]=false;
    for(int i=2;i*i<LIMIT;++i)
        if(isprime[i])
            for(int j=i*i;j<LIMIT;j+=i)
                isprime[j]=false;
}

long long find_divisor(long long x) {
    for (long long i = 2; i * i <= x; ++i) {
        if (x % i == 0) return i;
    }
    return -1;
}

int main() {
    cout << "Case #1:" << endl;
    int J, N;
    int cas;
    cin >> cas;
    cin >> N >> J;
    int found = 0;

    eratosthenes_sieve(MAX_PR);

    for (long long i = (1LL<<(N-1)) + 1; i < (1LL<<(N)); i += 2) {
        if (i < MAX_PR && isprime[i]) continue;
        vector<int> digits;
        long long tmp = i;
        while(tmp) {
            digits.push_back(tmp % 2);
            tmp /= 2;
        }
        reverse(digits.begin(), digits.end());
        vector<int> divisors(11, 0);
        for (long long b = 2; b <= 10; ++b) {
            long long res = 0;
            for (const int c : digits) {
                res = res * b + c;
            }
            long long div = -1;
            if (res >= MAX_PR || !isprime[res]) {
                div = find_divisor(res);
            }
            if (div == -1) break;
            divisors[b] = div;
        }
        if (divisors[10] != 0) {
            found++;
            for (int j = 0; j < digits.size(); ++j) {
                cout << digits[j];
            }
            cout << " ";
            for (int j = 2; j <= 10; ++j) {
                cout << divisors[j] << " ";
            }
            cout << endl;
            if (found == J) return 0;
        }
    }
}
