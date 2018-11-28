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
char s[MAXN];
void fun(int n)
{
    for(int i=0;i<=n;i++){
        if(s[i]=='+') s[i]='-';
        else s[i]='+';
    }
}
int main()
{
    int n, i, t, icase=0, ans;
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d",&t);
    while(t--){
        scanf("%s",s);
        printf("Case #%d: ",++icase);
        n=strlen(s);
        for(i=n-1;i>=0;i--){
            if(s[i]=='-'){
                n=i;
                break;
            }
        }
        if(i==-1){
            puts("0");
            continue ;
        }
        ans=0;
        for(i=1;i<=n;i++){
            if(s[i]!=s[i-1]) ans++;
        }
        printf("%d\n",ans+1);
    }
    return 0;
}

