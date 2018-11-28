#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <iterator>
#include <utility>
#include <iomanip>
#include <cctype>
#include <climits>
using namespace std;

#define MAX 50005

//int xx[]={1,0,-1,0};              int yy[]={0,1,0,-1}; //4 Direction
//int xx[]={1,1,0,-1,-1,-1,0,1};    int yy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int xx[]={2,1,-1,-2,-2,-1,1,2};   int yy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction

#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

#define REP(i,n)for (i=0;i<n;i++)
#define CLR(p) memset(p, 0, sizeof(p))
#define mset(p, v) memset(p, v, sizeof(p))
#define ALL(c) c.begin(), c.end()
#define SZ(c) (int)c.size()
#define pb(x) push_back(x)

#define ll long long int
#define vs vector<string>
#define vi vector<int>
#define vii vector< pair<int, int> >
#define pii pair< int, int >
#define psi pair< string, int >

#define fs first
#define sc second
#define MP(x, y) make_pair(x, y)

//#define LOG(x,BASE) (log10(x)/log10(BASE))
//#define EQ(a,b)     (fabs(a-b)<ERR)

///**biwise operation**/
//#define popc(i) (__builtin_popcount(i))

//#define csprint printf("Case %d: ", ++t);
//#define PI acos(-1)
//#define ERR 10E-5

const int INF = 0x7f7f7f7f;

template<class T> void deb(T e){cout<<e<<endl;}
template<class T1,class T2> void deb(T1 e1,T2 e2){cout<<e1<<"\t"<<e2<<endl;}
template<class T1,class T2,class T3> void deb(T1 e1,T2 e2,T3 e3){cout<<e1<<"\t"<<e2<<"\t"<<e3<<endl;}
template<class T1,class T2,class T3,class T4> void deb(T1 e1,T2 e2,T3 e3,T4 e4){cout<<e1<<"\t"<<e2<<"\t"<<e3<<"\t"<<e4<<endl;}
template<class T1,class T2,class T3,class T4,class T5> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5){cout<<e1<<"\t"<<e2<<"\t"<<e3<<"\t"<<e4<<"\t"<<e5<<endl;}

template<class T> void deb(vector<T> e){int i;REP(i,SZ(e)) cout<<e[i]<<" ";cout<<endl;}

//double deg2rad(double x){ return (PI*x)/180.0; }
//double rad2deg(double x){ return (180.0*x)/PI; }

template<class T> string toString(T n){ostringstream oss;oss<<n;oss.flush();return oss.str();}

ll Pow(ll B,ll P){  ll R=1; while(P>0)  {if(P%2==1) R=(R*B);P/=2;B=(B*B);}return R;}
int BigMod(ll B,ll P,ll M){ ll R=1; while(P>0)  {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return (int)R;}

///************************************* Coding Starts from here**************************************///
bool flag[10];
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ll i, n, j, k, u, v, w, x, y, z, t=0, tcase, res=0;



    cin>>tcase;
    for(t=1; t<=tcase; t++)
    {
        cin>>n;
        mset(flag, 0);
        bool isSolved= false;


        for(i=1; i<10000; i++)
        {
            x= n*i;
            stringstream ss;
            string str;

            ss<<x;
            ss>>str;

            bool isTakenAll=true;
            REP(k, SZ(str))
            {
                flag[str[k]-'0']= true;
            }

            REP(k, 10)
            {
                if(flag[k]== false )
                    isTakenAll= false;
            }

            if(isTakenAll==true)
            {
                isSolved= true;
                break;
            }
        }

        if(isSolved)
            printf("Case #%lld: %lld\n", t, n*i);
        if(!isSolved)
            printf("Case #%lld: INSOMNIA\n", t);
    }
    return 0;
}
