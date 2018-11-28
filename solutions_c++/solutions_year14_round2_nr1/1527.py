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
LL n,m,i,j,k,l,a[105][105],b[105],p[1000009],ans,cn,t,x,y,z,mx,mn,s,len,cnt;
char c[105][105],ch;
string d[105];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%I64d",&t);
    for(l=1;l<=t;l++)
    {
        for(i=0;i<105;i++)
        {
            d[i].clear();
        }
        cnt=0;
        scanf("%I64d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%s",c[i]);
            len=strlen(c[i]);
            cn=0;
            d[i].pub(c[i][0]);
            a[i][0]=1;
            for(j=1;j<len;j++)
            {
                if(c[i][j-1]!=c[i][j])
                {
                    d[i].pub(c[i][j]);
                    cn++;
                    cnt=max(cnt,cn);
                    a[i][cn]=1;
                }
                else
                {
                    a[i][cn]++;
                }
            }
        }
        sort(d,d+n);
        if(d[0]!=d[n-1])
        {
            printf("Case #%I64d: Fegla Won\n",l);
        }
        else
        {
            ans=0;
            for(i=0;i<=cnt;i++)
            {
                mem(b);
                for(j=0;j<n;j++)
                {
                    b[j]=a[j][i];
                }
                sort(b,b+n);
                s=0;
                for(j=0;j<n;j++)
                {
                    s+=fabs(b[j]-b[n/2]);
                }
                ans+=s;
            }
            printf("Case #%I64d: %I64d\n",l,ans);
        }
    }
    return 0;
}
