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
const int N=100010,MOD=1e9+7;


int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int T=in(),ca=1;
    while(T--)
    {
        ll n=in();
        if(!n)
        {
            printf("Case #%d: INSOMNIA\n",ca++);
            continue;
        }
        int ok=0,base=n;
        while(ok!=1023)
        {
            ll tmp=n;
            while(tmp)
            {
                int t=tmp%10;
                ok |= (1<<t);
                tmp/=10;
            }
            n += base;
        }
        printf("Case #%d: %I64d\n",ca++,n-base);
    }
    return 0;
}
