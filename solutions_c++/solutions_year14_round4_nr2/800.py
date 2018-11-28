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

int opc(int n, VI &v){
  //VI E;
  int res=0;
  FOR(i,n){
    int esq=0;
    int dre=0;
    for(int j=i+1;j<n;++j) if(v[j]>v[i]) ++dre;
//    for(int j=i-1;j<E.size();++j) if(E[j]>v[i]) ++esq;
    for(int j=i-1;j>=0;--j) if(v[j]>v[i]) ++esq;
   /* cerr<<v[i]<<' '<<min(dre,esq)<<' ';
    if(esq<dre) {
      //E.push_back(v[i]);
      cerr<<"esq"<<endl;
    }
    else cerr<<"dre"<<endl;*/
    res+=min(esq,dre);
  }
  return res;
}

int main(){
//  ios_base::sync_with_stdio(false);
  freopen("Bgreat.out","w",stdout);
  freopen("Bgreat.in","r",stdin);
  int casos;
  cin>>casos;
  FORU(cas,casos){
    int n;
    cin>>n;
    VI v(n);
    FOR(i,n) cin>>v[i];
    cout<<"Case #"<<cas<<": "<<opc(n,v)<<endl;
  }
  //system("pause");
}
