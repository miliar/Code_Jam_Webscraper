#include <cstdio>
#include <cmath>

using namespace std;

int main() {
    int T, t;
    long long int P, Q, ans;
    scanf("%d", &T);
    for(t = 0; t < T; ++t) {
        scanf("%lld/%lld", &P, &Q);
        ans = 0;
        if(Q == P) {
            ans = 1;
        } else if(Q&1) {
            ans = -1;
        } else {
            while((Q = Q >> 1) != 0) {
                ++ans;
                if(Q <= P) {
                    if(Q < P) {
                        P -= Q;
                    }
                    while((Q = Q >> 1) != 0) {
                        if(Q < P) {
                            P -= Q;
                        }
                        if(Q&1 && Q != 1) {
                            ans = -1;
                            break;
                        }
                    }
                    break;
                }
                if(Q&1) {
                    ans = -1;
                    break;
                }
            }
        }
        if(ans == -1) {
            printf("Case #%d: impossible\n", t+1);
        } else {
            printf("Case #%d: %d\n", t+1, ans);
        }
    }
    return 0;
}
