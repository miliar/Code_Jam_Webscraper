#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<queue>
#include<stack>
#include<map>
#include<time.h>
#include<cmath>
#include<vector>
#include <iomanip>
#define PB(u)  push_back(u);
#define AA   first
#define BB   second
#define inf 0x3f3f3f3f
#define mminf(u)  memset(u,0x3f,sizeof(u))
using namespace std ;
#define MAX 55
#define sz size()
typedef long long ll ;
typedef pair<int,int> PII ;
const double eps=1e-8;
const double pi=acos(-1.0);

ll a[9];
ll b[9] = {2,3,4,5,6,7,8,9,10};
ll d[50];
ll e[10];

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int T ;
    cin>>T;
    int cas=1;
    while(T--)
    {
        int n , m ;
        scanf("%d%d",&n,&m);
        ll nn = 1<<n;
        int sum = 0;
        printf("Case #%d:\n",cas++);
        for(ll i = 1<<(n-1) ; i < nn ; i++){
            if(i%2==0)
                continue;
            ll p = i/2;
            ll c[9];
            for(int j = 0 ; j < 9 ; j++){
                c[j] = b[j];
                a[j] = 1;
            }
            while(p){
                for(int j = 0 ; j < 9 ; j++){
                    a[j] += (ll)c[j]*(p%2) ;
                    c[j] *= (j+2);
                }
                p/=2;
            }
            int now = 0;
            for(int j = 0 ; j < 9 ; j++){
                now = 0;
                for(ll k = 2 ; k*k <= a[j] ; k++){
                    if(a[j] %k == 0){
                        e[j] = k;
                        now = 1;
                        break;
                    }
                }
                if(now==0)
                    break;
            }
            if(now==1){
                p = i;
                for(int j = 0 ; j < n ; j++){
                    d[j] = p%2;
                    p/=2;
                }
                for(int j = n-1 ; j >= 0 ; j--)
                    printf("%I64d",d[j]);
                for(int j = 0 ; j < 9 ; j++)
                    printf(" %I64d",e[j]);
                printf("\n");
                sum++;
            }
            if(sum >= m)
                break;
    }
    }
    return 0;
}


