#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <iostream>
using namespace std;

int cnt = 0;
int *primes;
bool *label;

const int BOUND = 100000000;
void pre() {
    cnt = 0;
    primes = (int*)malloc(sizeof(int) * 10000000);
    label = (bool*)malloc(sizeof(bool) * BOUND + 10);
    
    memset(primes, 0, sizeof(int) * 10000000);
    memset(label, false, sizeof(bool) * BOUND + 10);
    
    for (int i = 2; i <= 100000000; i++) {
        if (label[i] == false) {
            primes[cnt++] = i;
            for (int j = i + i; j <= BOUND; j += i) {
                label[j] = true;
            }
        }
    }
}

int res[65536][128] = {0};

long long transform(int num, int base) {
    long long b = 1LL;
    long long k = 0;

    while (num > 0) {
        if (num % 2 == 1) {
            k = k + b;
        }
        num /= 2;
        b *= base;
    }

    return k;
}

bool check(long long num) {
    for (long long base = 2; base <= 10; base++) {
        long long k = transform(num, base);

        /*
        if (k < BOUND) {
            if (label[k] == false) {
                return false;
            }
        } else {
        */
        bool isprime = true;
        for (int i = 0; i < cnt && 1LL * primes[i] * primes[i] < k; i++) {
            if (k % primes[i] == 0) {
                isprime = false;
                break;
            }
        }

        if (isprime) {
            return false;
        }
    }

    return true;
}

void fill(int num, int p) {
    res[p][0] = num;
    for (int base = 2; base <= 10; base++) {
        long long k = transform(num, base);
        for (int i = 0; i < cnt; i++) {
            if (k % primes[i] == 0) {
                res[p][base] = primes[i];
                break;
            }
        }
    }
}

int main(int argc, char *argv[])
{
    int T = 0;
    pre();

    cerr << "preprocess done, cnt = " << cnt << endl;
    
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        memset(res, 0, sizeof(res));
        int p = 0;

        int N = 0, J = 0;
        cin >> N >> J;
        for (int i = (1 << (N - 1)) + 1; i < (1 << N); i += 2) {
            if (check(i)) {
                if (p <= J) {
                    cerr << "check " << i << " pass" << endl;
                    fill(i, p);
                    p++;
                }
            } else {
                // cerr << "check " << i << " failed" << endl;
            }
        }
        cout << "Case #" << cas << ":" << endl;
        for (int i = 0; i < J; i++) {
            string s = "";
            int x = res[i][0];
            while (x > 0) {
                if (x % 2 == 1) {
                    s = s + "1";
                } else {
                    s = s + "0";
                }
                x /= 2;
            }
            reverse(s.begin(), s.end());

            cout << s;
            for (int j = 2; j <= 10; j++) {
                cout << " " << res[i][j];
            }
            cout << endl;
        }
    }
    return 0;
}
