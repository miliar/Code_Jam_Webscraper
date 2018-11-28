#include<bits/stdc++.h>
using namespace std;

#define X first
#define Y second
#define ii1 pair<char,int>
#define ii pair<char,char>
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define l long long
#define pb(x) push_back(x)
map< ii, ii1>mp1;
ifstream ifs("dj.in");
ofstream ofs("djd.out",ofstream::app);
int main()
{
    int t;
    ifs>>t;
    mp1[ii('1','1')]=ii1('1',0);
    mp1[ii('1','i')]=ii1('i',0);
    mp1[ii('1','j')]=ii1('j',0);
    mp1[ii('1','k')]=ii1('k',0);
    mp1[ii('i','1')]=ii1('i',0);
    mp1[ii('i','i')]=ii1('1',1);
    mp1[ii('i','j')]=ii1('k',0);
    mp1[ii('i','k')]=ii1('j',1);
    mp1[ii('j','1')]=ii1('j',0);
    mp1[ii('j','i')]=ii1('k',1);
    mp1[ii('j','j')]=ii1('1',1);
    mp1[ii('j','k')]=ii1('i',0);
    mp1[ii('k','1')]=ii1('k',0);
    mp1[ii('k','i')]=ii1('j',0);
    mp1[ii('k','j')]=ii1('i',1);
    mp1[ii('k','k')]=ii1('1',1);
    for(int j=1;j<=t;j++)
    {

         int L,X;
         ifs>>L>>X;
         string str;
         ifs>>str;
         ofs<<"Case #"<<j<<": ";
         string str1=str;
         for(int i=1;i<X;i++)str+=str1;
         ii1 ar[100009];
         ar[0].X=str[0];
         ar[0].Y=0;
         for(int i=1;i<L*X;i++)
         {
             ar[i].X=mp1[ii(ar[i-1].X,str[i])].first;
             ar[i].Y=ar[i-1].Y+mp1[ii(ar[i-1].X,str[i])].second;
         }
         int flag=0;
         if(ar[L*X-1].X=='1'&&ar[L*X-1].Y%2==1)
         {
             for(int i=0;i<L*X;i++)
             {
                if(ar[i].Y%2==0&&ar[i].X=='i')
                {
                     for(int j=i+1;j<L*X;j++)
                     {
                         if(ar[j].X=='k'&&ar[j].Y%2==0)
                         {
                             flag=1;
                             goto s;
                         }
                     }
                }
             }
         }
         s:
         if(flag==1)
         {
             ofs<<"YES"<<endl;
         }
         else
         {
             ofs<<"NO"<<endl;
         }


    }
}
