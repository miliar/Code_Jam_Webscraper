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
    for(int oo=1;oo<=t;oo++)
    {


    int a[5][5],b[5][5];
    int cnt=0;
    int n,k,ans=0;
    cin>>n;
   n--;
    rep(i,4)
    rep(j,4)
    cin>>a[i][j];

   cin>>k;
   k--;
   rep(i,4)
   rep(j,4)
    cin>>b[i][j];

    rep(i,4)
    rep(j,4)
    {
        if(a[n][i]==b[k][j])
        {
            cnt++;
            ans=a[n][i];

        }
    }
    cout<<"Case #"<<oo<<": ";
    if(cnt==1)
    {
        cout<<ans<<endl;

    }
    else if(cnt>1)
    {
     cout<<"Bad magician!"<<endl;
    }
    else
    {
        cout<<"Volunteer cheated!"<<endl;
    }
}
}
