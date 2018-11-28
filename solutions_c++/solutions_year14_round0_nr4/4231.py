//Done by Mycroft Grey
//Fet per Ferran Alet

#include<iostream>
#include<cmath>
#include<iomanip>
#include<vector>
#include<map>
#include<queue>
#include<fstream>
#include<algorithm>
#include<string>
#include<stack>
#include<numeric>
#include<set>
#include<sstream>
#include<list>

#define INF 2147483647
#define LINF 1000000000000000000LL
#define EPS 1e-9
#define debug(x) cerr << #x << " = " << x << endl
#define Debug(v) cerr << #v << " = "; for(int wow=0;wow<v.size();++wow) cerr<<v[wow]<<' '; cerr<<endl
#define FOR(x,y) for(int x=0;x<y;x++)
#define FORU(x,y) for(int x=1;x<=y;x++)
#define RFOR(x,y) for(int x=y-1;x>=0;--x)
using namespace std;


typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<double> VD;
typedef vector<VD> VVD;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<string> VS;
typedef map<int,int> MII;
typedef MII::iterator iMII;
typedef vector<PII > VP;

int main(){
  ios_base::sync_with_stdio(false);
  int casos;
  cin>>casos;
  FORU(cas,casos){
    int n;
    cin>>n;
    VD M(n),F(n);
    FOR(i,n) cin>>M[i];
    FOR(i,n) cin>>F[i];
    sort(M.begin(),M.end());
    sort(F.begin(),F.end());
   // Debug(M);
   // Debug(F);
    int b=0;
    int cont=0;
    FOR(i,n){
      while(b<n && F[b]<M[i]) ++b;
      if(b==n) break;
      cont++;
      ++b;
    }
    int cont2=n;
    FOR(i,n){
      bool bb=true;
      for(int j=i;j<n && bb;++j) if(M[j]<F[j-i]) {/*cerr<<M[j]<<'<'<<F[j-i]<<endl;*/ bb=false;}
      if(bb) {
        cont2=i;
        break;
      }
    }
    cout<<"Case #"<<cas<<": "<<n-cont2<<' '<<n-cont<<endl;
  }
 // system("pause");
}
