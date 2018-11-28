#include <iostream>
#include <string.h>
#include <math.h>
#include <queue>
#include <algorithm>
#include <stdlib.h>
#include <map>
#include <set>
#include <stdio.h>
#include <string>
#include <time.h>
using namespace std;
#define LL long long
#define pi acos(-1.0)

const int mod=1e9+7;
const int INF=0x3f3f3f3f;
const double eqs=1e-9;
const int MAXN=100+10;
int ha[12], cnt;
void fun(int x)
{
    while(x){
        int t=x%10;
        if(!ha[t]){
            cnt++;
            ha[t]=1;
        }
        x/=10;
    }
}
int main()
{
    int t, n, i, j, icase=0, x;
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        printf("Case #%d: ",++icase);
        if(!n){
            puts("INSOMNIA");
            continue ;
        }
        cnt=0;
        for(i=0;i<10;i++){
            ha[i]=0;
        }
        fun(n);
        x=2;
        while(1){
            fun(x*n);
            if(cnt==10) break;
            x++;
        }
        printf("%d\n",x*n);
    }
    return 0;
}

