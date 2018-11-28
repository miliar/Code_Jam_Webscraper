#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<list>
#include<iterator>

using namespace std;


#define FRO freopen("in.txt","r",stdin);
#define FRU freopen("out.txt","w",stdout);

#define SET(a) memset(a,-1,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define i64 long long
//#define i64 __int64
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define infinity 2147483647
#define pi 3.1415926535897932384626433832795028841971
#define eps 1e-9



#define foreach(i,n) for(__typeof((n).begin())i =(n).begin();i!=(n).end();i++)
#define in(n,a,b) ( n>=a && n<=b )


template< class T > T sqr(T n) { return n*n; }
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template< class T > T Max(T a, T b) { return a>b?a:b; }
template< class T > T Min(T a, T b) { return a<b?a:b; }
template< class T > T abs(T a) { return a>0?a:-a; }

//const int row[]={-1, -1, -1,  0,  0,  1,  1,  1};  // Kings Move
//const int col[]={-1,  0,  1, -1,  1, -1,  0,  1};  // Kings Move
//const int row[]={-2, -2, -1, -1,  1,  1,  2,  2};  // Knights Move
//const int col[]={-1,  1, -2,  2, -2,  2, -1,  1};  // Knights Move
//const int row[]={-1,0,0,1,0};
//const int col[]={0,-1,1,0,0};

#define MOD 1000000009
#define Limit 100005

int n,m;
char s[110];

bool nc(int i)
{
    return (s[i]!='a'&&s[i]!='e'&&s[i]!='i'&&s[i]!='o'&&s[i]!='u');
}

int main()
{
    FRO
    FRU
    int tc,t,i,j,k,a,b,c,d;
    cin>>tc;
    for(t=1;t<=tc;t++)
    {
        cin>>s>>n;
        int sum=0;
        int ar[110];
        CLR(ar);
        int len=strlen(s);


        for(i=0;i<len;i++)
        {
            for(j=i;j<len;j++)
            {
                CLR(ar);
                if(nc(i))ar[i]=1;
                a=ar[i];
                for(k=i+1;k<=j;k++)
                {
                    if(nc(k))ar[k]+=ar[k-1]+1;
                    else ar[k]=0;
                    a=Max(a,ar[k]);
                }
                if(a>=n)sum++;
            }
        }
        printf("Case #%d: %d\n",t,sum);
    }
    return 0;
}

