#include<iostream>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<cmath>
#include<sstream>
#define REP(i,n) for(int i=0;i<n;++i)
#define FOR(i,j,k) for(int i=j;i<k;++i)
#define REPD(i,n) for(int i=n;i>-1;--i)
#define ALL(v) v.begin(),v.end()
#define ll long long
#define PB push_back
using namespace std;

bool isPal(int i){
      ostringstream  is;
      is<<i;
      string s = is.str();
      int n = s.size();
      REP(i,n/2) if(s[i]!=s[n-i-1]) return false;
      
      
      return true;
     }

int main()
{
    int ts;cin>>ts;
    REP(tn,ts)
    {
        int a , b; cin>>a>>b;
        ll ret = 0;
        FOR(i,a,b+1){
                             int c = (int) sqrt(i);
                             if(c*c<i) continue;
                             if(isPal(i) && isPal(c)) ++ret;
                     }

        cout<<"Case #"<<(tn+1)<<": "<<ret<<endl;
    }
}
