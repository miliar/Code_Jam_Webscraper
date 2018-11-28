#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

int T=1, N=32, J=500;
int number[64];

bool isPrime[10000];
vector<int> prime;
void sieve() {
    memset(isPrime, true, sizeof(isPrime));
    for(int i=2; i<10000; i++) {
        if (isPrime[i]) {
            prime.push_back(i);
            for(int j=i+i; j<10000; j+=i) isPrime[j] = false;
        }
    }
}

int remainder(int p, int b) {
    int r = 0;
    for(int i=0; i<N; i++) {
        r = (r*b)%p;
        r = (r+number[i])%p;
    }
    return r;
}

int main() {
    //freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    sieve();

    for(int ncase=1; ncase<=T; ncase++) {
        printf("Case #%d:\n", ncase);

        number[0] = number[N-1] = 1;

        int cnt=0;
        while(cnt<J) {
            vector<int> proof;
            for(int base=2; base<11; base++) { // maybe stop if we already couldnt get a proof to one base
                for(int i=0; i<prime.size(); i++) {
                    if (remainder(prime[i], base) == 0) {
                        proof.push_back(prime[i]);
                        break;
                    }
                }
            }

            if (proof.size() == 9) {
                cnt++;
                for(int i=0; i<N; i++) printf("%d", number[i]);
                for(int i=0; i<9; i++) printf(" %d", proof[i]);
                printf("\n");
            }

            /* incrementing number */
            for(int i=N-2; ; i--) {
                if (number[i] == 0) {
                    number[i] = 1;
                    break;
                }
                else {
                    number[i] = 0;
                }
            }
        }
    }

    return 0;
}
