#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <string>
#include <vector>
#include <cmath>

//#define __OJ__
using namespace std;

long long isPrime(string s, int base) {
    long long data = 0;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '1')
            data += pow(base, s.size() - i - 1);
    }
    for (long long i = 2; i * i < data; i++) {
        if (data % i == 0)
            return i;
    }
    return -1;
}

bool isCoinJam(string s, vector<long long>& divisors) {
    divisors.clear();
    for (int i = 2; i <= 10; i++) {
        long long divisor = isPrime(s, i);
        if (divisor != -1)
            divisors.push_back(divisor);
        else
            return false;
    }
    return true;
}

string next(string s) {
    int i = s.size() - 1;
    while (i >= 0) {
        if (s[i] == '0') {
            s[i] = '1';
            break;
        }
        else {
            s[i] = '0';
        }
        i--;
    }
    return s;
}

int main() {
#ifdef __OJ__
    freopen("//Users//jiahuiguo//GitHub//Problems//GoogleCodeJam//CoinJam//C-small-attempt0.in", "r", stdin);
    freopen("//Users//jiahuiguo//GitHub//Problems//GoogleCodeJam//CoinJam//C-small-attempt0.out", "w", stdout);
#endif
    int T;
    scanf("%d", &T);
    int N, J;
    scanf("%d %d\n", &N, &J);
    printf("Case #1:\r\n");
    vector<long long> divisors;
    string s(N - 2, '0');
    string coin;
    while (J > 0) {
        coin = "1" + s + "1";
        if (isCoinJam(coin, divisors)) {
            printf("%s", coin.c_str());
            for (auto divisor : divisors)
                printf(" %lld", divisor);
            printf("\r\n");
            J--;
        }
        s = next(s);
    }
    return 0;
}