//Bismillahir Rahmanir Rahim
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cctype>
#include<cassert>
#include<cstdlib>
#include<iostream>
#include<iomanip>
#include<string>
#include<sstream>
#include<algorithm>
#include<vector>
#include<stack>
#include<list>
#include<queue>
#include<set>
#include<map>
#include<utility>
#include<bitset>
#include<ctime>
using namespace std;

#define i64 long long int
#define u64 unsigned long long int

#define fin(a) freopen(a,"r",stdin)
#define fout(a) freopen(a,"w",stdout)

#define repc(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)
#define repr(i,a,b) for(__typeof(b) i=(a); i>=(b); i--)

#define clr(a) a.clear()
#define sz(a) (int)a.size()
#define mem(a,b) memset(a,b,sizeof a)
#define ERASE(a) a.erase(a.begin(),a.end())

#define sc scanf
#define S(z) scanf("%d",&z)
#define S2(xx,zz) scanf("%d %d",&xx,&zz)
#define SC(z) scanf("%s",&z)

#define pf printf
#define pfn printf("\n")
#define PF(z) printf("%d",z)
#define PF2(x,y) printf("%d %d",x,y)
#define PFL(z) printf("%I64d",z)
#define PFS(z) printf("%s",z)

#define MI map<int,int>
#define MSI map<string,int>
#define MIS map<int,string>
#define SI set<int>
#define SS set<string>
#define SMI multiset<int>
#define VI vector<int>
#define VI2 vector < vector < int > >
#define QU queue<int>
#define PQU priority_queue<int>
#define STK stack<int>
#define pb push_back

#define inf 2000000000
#define pi  acos(-1.0)
#define MAX 1000007
#define MOD 1000000007
#define eps 1e-9

template <class T>T sqr(T x) {return x*x;}
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template <class T> inline T bigmod(T p,T e,T M)
{
    if(e==0) return 1;
    if(e%2==0){i64 t=bigmod(p,e/2,M);return (T)((t*t)%M);}
    return (T)((i64)bigmod(p,e-1,M)*(i64)p)%M;
}
template <class T> inline T bigexp(T p,T e)
{
    if(e==0)return 1;
    if(e%2==0){i64 t=bigexp(p,e/2);return (T)((t*t));}
    return (T)((i64)bigexp(p,e-1)*(i64)p);
}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}

int dx4[]={1,0,-1,0};int dy4[]={0,1,0,-1}; //4 Direction
int dx8[]={1,1,0,-1,-1,-1,0,1};int dy8[]={0,1,1,1,0,-1,-1,-1};//8 direction
int month[]={31,28,31,30,31,30,31,31,30,31,30,31};
/*
struct Graph
{
    int u,v,w;
    bool operator<(const Graph& p)
    const {return w<p.w;} // oporerta chotor jnne
}edge[10];

vector<int>edges,cost;
*/
/******************* Code Starts here *******************/

int t,x,r,c,co;
char s[6][6][6],ch;
int main()
{
    fin("D-small-attempt0.in");
    fout("D_output_final_output.txt");
    S(t);
    s[2][1][1]='R';s[2][1][2]='G';s[2][1][3]='R';s[2][1][4]='G';
    s[2][2][1]='G';s[2][2][2]='G';s[2][2][3]='G';s[2][2][4]='G';
    s[2][3][1]='R';s[2][3][2]='G';s[2][3][3]='R';s[2][3][4]='G';
    s[2][4][1]='G';s[2][4][2]='G';s[2][4][3]='G';s[2][4][4]='G';

    s[3][1][1]='R';s[3][1][2]='R';s[3][1][3]='R';s[3][1][4]='R';
    s[3][2][1]='R';s[3][2][2]='R';s[3][2][3]='G';s[3][2][4]='R';
    s[3][3][1]='R';s[3][3][2]='G';s[3][3][3]='G';s[3][3][4]='G';
    s[3][4][1]='R';s[3][4][2]='R';s[3][4][3]='G';s[3][4][4]='R';

    s[4][1][1]='R';s[4][1][2]='R';s[4][1][3]='R';s[4][1][4]='R';
    s[4][2][1]='R';s[4][2][2]='R';s[4][2][3]='R';s[4][2][4]='R';
    s[4][3][1]='R';s[4][3][2]='R';s[4][3][3]='R';s[4][3][4]='G';
    s[4][4][1]='R';s[4][4][2]='R';s[4][4][3]='G';s[4][4][4]='G';
    while(t--)
    {
      sc("%d %d %d",&x,&r,&c);
      if(x==1)
      {
        pf("Case #%d: GABRIEL\n",++co);
      }
      else
      {
        ch=s[x][r][c];
        if(ch=='G')
          pf("Case #%d: GABRIEL\n",++co);
        else
        {
          pf("Case #%d: RICHARD\n",++co);
        }
      }
    }
    return 0;
}


