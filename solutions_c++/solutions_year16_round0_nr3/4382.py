#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <cstring>
#include <array>

using namespace std;

typedef unsigned long long ll;

int T,N,J;
int C;
int B[32];
int ff[11];

int modpow(int base, int exp, int modulus) {
    base %= modulus;
    int result = 1;
    while (exp > 0) {
        if (exp & 1) result = (result * base) % modulus;
        base = (base * base) % modulus;
        exp >>= 1;
    }
    return result;
}

void next_byte() {
    B[0] = 1; B[N-1] = 1;
    for (int i = 1; i <= N-2; ++i) {
        if (B[i]==0) {B[i] = 1; return;}
        if (B[i]==1) B[i] = 0;
    }
}

bool check_factor(unsigned int f, unsigned int b) {
    int res = 0;
    for (int i = 0; i < N; ++i) {
        if (B[i]==1) {
            res += modpow(b, i, f);
            res = res % f;
        }
    }
    return res%f == 0;
}

int look_for_factor(int b) {
    if (check_factor(2, b)) return 2;
    for (int n = 3; n <= C; n+=2) {
        if (check_factor(n, b)) return n;
    }
    return -1;
}

void print_out() {
    for (int i = N-1; i>=0; --i) printf("%d",B[i]);
    for (int b = 2; b<=10; ++b) printf(" %d",ff[b]);
    printf("\n");
}

int main(int argc, const char * argv[]) {
    freopen(argv[1], "r", stdin);
    
    scanf("%d%d%d\n",&T,&N,&J);
    memset(B, 0, sizeof(B));
    printf("Case #1:\n");
    
    C = (int) sqrt(pow(2, N));
    
    while(J-->0) {
        bool got = false;
        while(!got) {
            next_byte();
            got = true;
            for (int b = 2; b <= 10; ++b) {
                ff[b] = look_for_factor(b);
                if (ff[b]==-1) {
                    got = false;
                    break;
                }
            }
        }
        if (!got) printf("WTF!\n");
        print_out();
    }
    
    return 0;
}
