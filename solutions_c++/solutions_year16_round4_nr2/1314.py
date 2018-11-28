/*    brioso     */
#include <bits/stdc++.h>
//#include <iostream>
//#include <cstdio>
//#include <algorithm>
//#include <cstring>
//#include <cmath>
//#include<set>
//#include<map>
//#include<queue>

using namespace std;
#define MAXN 1005
#define inf 0x3f3f3f3f
typedef long long ll ;
const double eps =1e-8;
const int mod = 1000000007;
typedef pair<int, int> P;
const double PI = acos(-1.0);

double a[MAXN];
double b[MAXN];
int c[MAXN];
char s[MAXN];
int dp[MAXN];
bool vis[MAXN];
int n,m;
int ans;


int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("1.out","w",stdout);
    int t,ca = 1;
    int p,q;
    scanf("%d",&t);
    while(t--){
        scanf("%d %d",&n,&m);
        for(int i = 0 ; i < n ; i++)
            scanf("%lf",&a[i]);
        sort(a,a+n);
        int cnt = 0;
        double nn = 0;
        for(ll i = 0 ; i < 1<<n ; i++){
            int sum = 0;
            for(int j = 0 ; j< n ; j++){
                if((1<<j)&i)
                    sum++;
            }
            if(sum != m)
                continue;
            vector<double> b;
            for(int j = 0 ; j < n ; j++){
                if(i & 1<<j)
                    b.push_back(a[j]);
            }
            double ans = 0;
            for(int j = 0  ; j < 1<<m ; j++){
                int sum = 0;
                for(int k = 0 ; k< m ; k++){
                    if((1<<k)&j)
                        sum++;
                }
                if(sum != m/2)
                    continue;
                double res = 1;
                for(int k = 0 ; k < m ; k++){
                    if((1<<k)&j)
                        res *= b[k];
                    else res *= (1-b[k]);
                }
                ans += res;
            }
            nn = max(nn,ans);
        }
        printf("Case #%d: ",ca++);
        printf("%.8lf\n",nn);
    }
    return 0;
}


/*

unsigned   int   0～4294967295
int   2147483648～2147483647
unsigned long 0～4294967295
long   2147483648～2147483647
long long的最大值：9223372036854775807
long long的最小值：-9223372036854775808
unsigned long long的最大值：18446744073709551615

__int64的最大值：9223372036854775807
__int64的最小值：-9223372036854775808
unsigned __int64的最大值：18446744073709551615

*/
