#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>
 
using namespace std;
 
typedef unsigned long long ULL;
typedef long long LL;
typedef long double LD;
typedef pair<int, int> PII;
typedef map<int, int> MI;
typedef vector<int> VI;
typedef vector<vector<int> > VVI;
const double pi=acos(-1.0);
const double eps=1e-11;
const int mod = 1e9 + 7;
 
#define two(X) (1<<(X))
#define twoL(X) ((1LL)<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
 
#define rep(i, n) rb(i, 0, n)
#define rb(i, b, n) rbc(i, b, n, <)
#define rbe(i, b, n) rbc(i, b, n, <=)
#define rbc(i, b, n, c) for(int i = ((int)(b)); i c ((int)(n)); i++)
 
#define p(x) cout << x;
#define ps(x) cout << x << " "
#define pl cout << endl
#define pn(x) cout << x << endl
 
#define s(v) ((int) v.size())
#define all(v) v.begin(), v.end()
#define MP make_pair
#define PB push_back
#define X first
#define Y second
#define getcx getchar
//_unlocked
 
template<class T>
inline void readInt( T &n )//fast input function
{
   n=0;
   T ch=getcx();int sign=1;
   while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}
 
   while(  ch >= '0' && ch <= '9' )
           n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
   n=n*sign;
}
int main()
{
    int t;
    cin>>t;
    double no[1001],ko[1001],ko1[1001];
    for(int oo=1;oo<=t;oo++)
    {
        int ans1=0,ans2=0;
        int n;
        cin>>n;
        rep(i,n)
        cin>>no[i];
        sort(no,no+n);
        rep(i,n)
        cin>>ko[i];
        sort(ko,ko+n);
        rep(i,n)
        ko1[i]=ko[i];
        int i=0,j=0;
        rep(i,n)
        {
 
               rep(j,n)
               {
                   if(no[i]>ko1[j])
                   {
                       ans1++;
                       ko1[j]=10;
                       break;
                   }
               }
 
 
        }
 
        rep(i,n)
        {
             rep(j,n)
                {
                    if(ko[i]>no[j])
                    {
                        no[j]=10;
                        ans2++;
                       // cout<<ko[i]<<"  ";
                        //cout<<no[j]<<endl;
                        break;
                     }
                }
 
 
        }
ans2=n-ans2;
 
 
        cout<<"Case #"<<oo<<": "<<ans1<<" "<<ans2<<endl;
}
}
 