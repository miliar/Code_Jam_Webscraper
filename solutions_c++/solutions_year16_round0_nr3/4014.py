#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#define ll long long

using namespace std;

ll a[33];
ll ans[501][33];
ll ansNT[501][10];
ll nt[10];

int main() {

    int T;
    int test_case;
    ll N,J;

    scanf("%d",&T);

    for(test_case = 1; test_case <= T; test_case++) {
        scanf("%lld %lld",&N,&J);
        memset(a,0,sizeof(a));
        memset(ans,0,sizeof(ans));
        memset(ansNT,0,sizeof(ansNT));
        memset(nt,0,sizeof(nt));

        printf("Case #%d:\n", test_case);
        a[0] = 1; a[N-1] = 1;
        ll bound = 2 << (N-3);
        ll JIndex = 0;
        for(ll mid=0; mid<bound; mid++) {
            ll temp = mid;
            ll midIndex = N-2;
            while(temp > 0) {
                a[midIndex] = temp & 1;
                temp >>= 1;
                midIndex--;
            }

            ll base = 2;
            ll numOfPrime = 0;
            while(base <= 10) {
                ll sum = 0;
                ll exp = 1;
                for(ll i=N-1; i>=0; i--) {
                    sum += a[i] * exp;
                    exp *= base;
                }
                for(ll i=2; i*i<sum; i++) {
                    if(sum%i==0) {
                        nt[base] = sum/i;
                        numOfPrime++;
                        break;
                    }
                }
                base++;
            }

            if(numOfPrime == 9) {
                if(JIndex == J) break;
                for(ll i=0; i<N; i++) {
                    ans[JIndex][i] = a[i];
                    printf("%lld",ans[JIndex][i]);
                }
                for(ll i=2; i<=10; i++) {
                    ansNT[JIndex][i] = nt[i];
                    printf(" %lld",ansNT[JIndex][i]);
                }
                puts("");
                JIndex++;
            } 
        }
    }

    return 0;
}


