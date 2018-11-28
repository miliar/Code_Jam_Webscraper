#include <map>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <queue>
using namespace std;
map<string, int> id_map;
int id(const string& s){
  if (id_map.find(s)==id_map.end()){
    int cou = id_map.size();
    id_map[s] = cou;
  }
  return id_map[s];
}
int n, m;
string line;
vector<int> v[200];
int C[5000][5000];
vector<int> ngb[5000];
void add_edge(int v, int w, int c){
  C[v][w]+=c;
  ngb[v].push_back(w);
  ngb[w].push_back(v);
}
int par[5000];
int increase_flow(int s, int t){
  queue<int> q;
  for (int i=0;i<n+m+m;++i)
    par[i]=-1;
  q.push(s);
  par[s]=s;
  while (!q.empty()){
    int w = q.front();
    q.pop();
    for (int i=0;i<ngb[w].size();++i)
      if (C[w][ngb[w][i]]>0 && par[ngb[w][i]]==-1){
        par[ngb[w][i]] = w;
        q.push(ngb[w][i]);
      }
  }
  if (par[t]==-1)
    return 0;
  int w = t;
  while (w!=s){
    C[par[w]][w] -= 1;
    C[w][par[w]] += 1;
    w = par[w];
  }
  return 1;
}
const int inf = 10000;
int main(){
  int tnum;cin>>tnum;
  int tcou=0;
  while (tnum--){
    id_map.clear();
    cin>>n;getline(cin, line);
    for (int i=0;i<n;++i){
      getline(cin, line);
      stringstream ss(line);
      string s;
      vector<int> c;
      while (ss>>s){
        c.push_back(id(s));
      }
      v[i] = c;
    }
    m = id_map.size();
    for (int i=0;i<n+m+m;++i){
      ngb[i].clear();
      for (int j=0;j<n+m+m;++j)
        C[i][j]=0;
    }
    for (int i=0;i<n;++i){
      for (int j=0;j<v[i].size();++j){
        add_edge(i, n+v[i][j], inf);
        add_edge(n+m+v[i][j], i, inf);
      }
    }
    for (int i=0;i<m;++i)
      add_edge(n+i, n+m+i, 1);
    int ans = 0;
    while (increase_flow(0, 1))
      ++ans;
    cout<<"Case #"<<++tcou<<": "<<ans<<endl;
  }
  return 0;
}
