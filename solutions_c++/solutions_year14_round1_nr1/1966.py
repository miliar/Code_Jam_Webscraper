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
string s[155],s2[155],s3[155];
int flag[100];
int main()
{
    int t;
    cin>>t;
    for(int oo=1;oo<=t;oo++)
    {


    int n,l;
    cin>>n>>l;
    rep(i,n)
    cin>>s[i];

    rep(i,n)
    cin>>s2[i];

    sort(s,s+n);
    sort(s2,s2+n);


    flag[100]={0};

    rep(i,l)
    {
        if(s[0].substr(i,1).compare(s2[0].substr(i,1))==0)
            flag[i]=0;
        else
            flag[i]=1;
    }


    int ans=155,tans=0;
    rep(i,n)
    {
        s3[i]=s2[i];
    }
    int fg=0,fg2=0;

        rep(j,n)
        {
            tans=0;
            fg=0,fg2=0;
            rep(k,l)
            {
                if(s[0].substr(k,1).compare(s3[j].substr(k,1))!=0)
                {
                    flag[k]=1;
                }
                else
                    flag[k]=0;
            }
               
            rep(i,n)
            {
                rep(k,l)
                {
                    if(flag[k]==1)
                    {
                        if(s3[i][k]=='1')
                            s3[i][k]='0';
                        else
                            s3[i][k]='1';
                    }
                }
            }

            sort(s3,s3+n);



            rep(u,n)
            {

                      //  if(s[u][k]!=s3[u][k])

                    if(s[u].compare(s3[u])!=0)
                    {


                        fg=1;


                    }


            }

            if(fg==0)
            {

                   

            rep(k,l)
                tans+=flag[k];

            ans=min(ans,tans);
            }

            rep(k,n)
            s3[k]=s2[k];
    }
    cout<<"Case #"<<oo<<": ";

   // cout<<ans<<endl;
    if(ans==155)
        cout<<"NOT POSSIBLE"<<endl;
    else
        cout<<ans<<endl;


}
}
