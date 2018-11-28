#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<map>
#include<string>
#include<iostream>
#include<vector>
#include<queue>
#include<stack>
#include<cmath>
#include<ctype.h>
#include<deque>
#include<list>
#include<set>
#define INF 999999999
#define NEG -999999999
#define pi acos(-1.0)
#define LL long long int
#define LU unsigned long long int
#define EPS 1e-9
#define MOD 100000007
#define mem(a) memset(a,0,sizeof(a))

using namespace std;
int n,m,i,j,k,l,a[1000009],b[1000009],p[1000009],ans,cn,t,x,y,z,mx,mn,s;
char c[1000009],d[1000009],ch;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%s %d",c,&n);
        l=strlen(c);
        ans=0;
        for(j=0;j<l;j++)
        {
            cn=0;
            for(k=j;k<l;k++)
            {
                if((c[k]!='a')&&(c[k]!='e')&&(c[k]!='i')&&(c[k]!='o')&&(c[k]!='u'))
                {
                    cn++;
                }
                else
                {
                    cn=0;
                }
                if(cn==n)
                {
                    ans+=(l-k);
                    break;
                }
            }
        }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
