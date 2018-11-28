#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> PI;
typedef long long LL;
typedef double D;
#define FI first
#define SE second
#define MP make_pair
#define PB push_back
#define R(I,N) for(int I=0;I<N;I++)
#define F(I,A,B) for(int I=A;I<B;I++)
#define FD(I,N) for(int I=N-1;I>=0;I--)
#define make(A) scanf("%d",&A)
#define make2(A,B) scanf("%d%d",&A,&B)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define db if(1)printf
template<typename C> void maxi(C& a,C b){if(a<b)a=b;}
template<typename C> void mini(C& a,C b){if(a>b)a=b;}
#define MAXn 51000
#define MAX 26000
const int INF = 1000 * 1000 * 1000 + 3;
vector<int> e;
vector<PI> d[MAXn],d2[MAXn];
int N,odl[MAXn],gd[MAXn];
void init(int n){
  N = n;
  e.clear();
  R(i,n)d[i].clear();
}
void add_edge(int a,int b){
  d[a].PB(MP(b,int(e.size())));
  e.PB(1);
  d[b].PB(MP(a,int(e.size())));
  e.PB(1);
}
bool bfs(){
  R(i,N){
    d2[i].clear();
    gd[i]=0;
    odl[i]=-1;
  }
  queue<int> kol;
  kol.push(0);odl[0]=0;
  while(!kol.empty()){
    int ak = kol.front();kol.pop();
    R(i,d[ak].size()){
      if(e[d[ak][i].SE]==0)continue;
      int pom = d[ak][i].FI;
      if(odl[pom] == -1){
        odl[pom] = odl[ak]+1;
        kol.push(pom);
      }
      if(odl[pom] == odl[ak]+1)
        d2[ak].PB(d[ak][i]);
    }
  }
  return odl[1]!=-1;
}
int dfs(int nr,int flow){
  if(nr == 1 || flow == 0)return flow;
  int wyn = 0;
  F(i,gd[nr],d2[nr].size()){
    PI pom = d2[nr][i];
    int il = dfs(pom.FI,min(flow,e[pom.SE]));
    wyn += il;
    flow -= il;
    e[pom.SE] -= il;
    e[pom.SE^1] += il;
    if(flow == 0){
      gd[nr] = i;
      return wyn;
    }
  }
  gd[nr] = d2[nr].size();
  return wyn;
}
int flow(){
  int wyn=0;
  while(bfs())wyn+=dfs(0,INF);
  return wyn;
}
map<string, vector<int>> x;
int n;
void test(){
  x.clear();
  cin >> n;
  string ln1;
  getline(cin,ln1);
  R(i,n){
    getline(cin, ln1);
    stringstream ss(ln1);
    string pom;
    while(ss >> pom){
      x[pom].PB(i);
    }
  }
  init(n + x.size());
  int kt = n;
  for(auto el: x){
    for(auto sl: el.SE){
      add_edge(kt,sl);
    }
    kt++;
  }
  static int cas = 0;cas++;
  cout << "Case #" << cas << ": " << flow() << "\n";
}
main(){
  ios_base::sync_with_stdio(0);
  int _;cin >> _;while(_--)test();
}
