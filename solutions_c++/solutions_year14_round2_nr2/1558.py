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
#define inf (1<<30)
#define pi acos(-1.0)
#define LL long long int
#define LU unsigned long long int
#define eps 1e-9
#define mod 100000007
#define mem(a) memset(a,0,sizeof(a))
#define neg(a) memset(a,-1,sizeof(a))
#define pub(a) push_back(a)
#define pob(a) pop_back(a)
#define puf(a) push_front(a)
#define pof(a) pop_front(a)
#define mkp(a,b) make_pair(a,b)

using namespace std;
int n,m,i,j,k,l,a[1000009],b[1000009],p[1000009],ans,cn,t,x,y,z,mx,mn,s;
char c[1000009],d[1000009],ch;
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(l=1;l<=t;l++)
    {
        scanf("%d %d %d",&x,&y,&z);
        ans=0;
        for(i=0;i<x;i++)
        {
            for(j=0;j<y;j++)
            {
                if((i&j)<z)
                {
                    ans++;
                }
            }
        }
        printf("Case #%d: %d\n",l,ans);
    }
    return 0;
}
