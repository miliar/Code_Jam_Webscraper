/*

To believe is to know that every day

is a new beginning.

It is to trust that miracles happen,

and dreams really do come true.

To believe is to know that wonderful surprises

are just waiting to happen.

And all our hopes and dreams are within reach.

If only we believe.

*/
#include<bitset>
#include<map>
#include<vector>
#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
#include<cmath>
#include<stack>
#include<queue>
#include<set>
#define inf 0x3f3f3f3f
#define mem(a,x) memset(a,x,sizeof(a))
#define F first
#define S second
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;

inline int in()
{
    int res=0;char c;int f=1;
    while((c=getchar())<'0' || c>'9')if(c=='-')f=-1;
    while(c>='0' && c<='9')res=res*10+c-'0',c=getchar();
    return res*f;
}
const int N=1002,MOD=1e9+7;
char a[N];

int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int T=in(),ca=1;
    while(T--)
    {
        scanf("%s",a);
        int n=strlen(a);
        int ans=0;
        for(int i=n-1;i>=0;i--)
        {
            if(a[i]=='-')
            {
                ans++;
                for(int j=i;j>=0;j--) a[j]=(a[j]=='-')? '+' : '-';
            }
        }
        printf("Case #%d: %d\n",ca++,ans);
    }
    return 0;
}
