#include <iostream>
#include <string.h>
#include <math.h>
#include <queue>
#include <algorithm>
#include <stdlib.h>
#include <map>
#include <set>
#include <stdio.h>
using namespace std;
#define LL long long
#define PI acos(-1.0)
const int mod=1e7+3;
const LL INF=(LL)1e12;
const double eqs=1e-9;
char s[2000];
int main()
{
        freopen("1.in","r",stdin);
        freopen("A.out","w",stdout);
        int t, n, i, ans, tmp, Case=0;
        scanf("%d",&t);
        while(t--){
                scanf("%d",&n);
                scanf("%s",s);
                ans=tmp=0;
                //printf("%d\n",n);
                for(i=0;i<=n;i++){
                        if(s[i]!='0'&&tmp<i){
                                ans+=i-tmp;
                                tmp+=s[i]-'0'+i-tmp;
                        }
                        else tmp+=s[i]-'0';
                }
                printf("Case #%d: %d\n",++Case,ans);
        }
        return 0;
}
