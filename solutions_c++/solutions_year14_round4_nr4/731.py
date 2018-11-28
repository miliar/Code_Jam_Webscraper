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
typedef vector<VS> VVS;

int worst;
int compta;
int total;
VS S;

void recurs(int pos, VI &g, int n){
  if(pos==g.size()){
    int cont=total;
    VVS v(n);
    FOR(i,S.size()) v[g[i]].push_back(S[i]);
    FOR(i,n){
      if(v[i].size()==0) --cont;
      sort(v[i].begin(),v[i].end());
      for(int pos=1;pos<v[i].size();++pos){
        FOR(j,min(v[i][pos].size(),v[i][pos-1].size())) {
          if(v[i][pos-1][j]==v[i][pos][j])--cont;
          else break;
        }
      }
    }
    if(cont==worst) ++compta;
    if(cont>worst){
      compta=1;
      worst=cont;
    }
    return;
  }
  FOR(i,n) {g[pos]=i; recurs(pos+1,g,n);}
  return;
}

int main(){
//  ios_base::sync_with_stdio(false);
  freopen("D-easy2.out","w",stdout);
  freopen("D-easy2.in","r",stdin);
  int casos;
  cin>>casos;
  FORU(cas,casos){
    int n,m;
    cin>>m>>n;
    S= VS(m);
    total=n;
  //  cerr<<"HEY"<<endl;
    FOR(i,m) {
      cin>>S[i];
      total+=S[i].size();
    }
    VI v(m);
    worst=0;
    compta=0;
    recurs(0,v,n);
    cout<<"Case #"<<cas<<": "<<worst<<' '<<compta<<endl;
  }
 // system("pause");
}
