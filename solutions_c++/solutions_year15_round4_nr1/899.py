#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<char> vc;
typedef vector<vc> vvc;
typedef pair<int,char> ic;

int r,c;
vvc mapa;

int main(){
  int t; cin >> t;
  for(int cass = 1; cass <= t; ++cass){
    cin >> r >> c;
    mapa = vvc(r,vc(c));
    vector<set<ic> > rows(r),cols(c);
    for(int i = 0; i < r; ++i){
      for(int j = 0; j < c; ++j){
// 	cout << i << ' ' << j << endl;
	cin >> mapa[i][j];
// 	cout << mapa[i][j] << endl;
	if(mapa[i][j] != '.'){
	  rows[i].insert(ic(j,mapa[i][j]));
	  cols[j].insert(ic(i,mapa[i][j]));
	}
      }
    }
    int cont = 0;
    bool ended = false;
    for(int i = 0; i < r; ++i){
      if(rows[i].size() == 0) continue;
      if(rows[i].size() == 1){
	set<ic>::iterator it = rows[i].begin();
	ic aux = *it;
	int j = aux.first;
	if(cols[j].size() == 1){
	  cout << "Case #" << cass << ": " << "IMPOSSIBLE" << endl;
	  ended = true;
	  break;
	}
	char cc = aux.second;
	if(cc == '<' or cc == '>') cont++;
      }
      else{
	set<ic>::iterator it = rows[i].begin();
	ic aux1 = *it;
	it = rows[i].end(); --it;
	ic aux2 = *it;
	if(aux1.second == '<') ++cont;
	if(aux2.second == '>') ++cont;
      }
    }
    if(ended) continue;
    for(int j = 0; j < c; ++j){
      if(cols[j].size() == 0) continue;
      else{
	set<ic>::iterator it = cols[j].begin();
	ic aux1 = *it;
	it = cols[j].end(); --it;
	ic aux2 = *it;
	if(aux1.second == '^') ++cont;
	if(aux2.second == 'v') ++cont;
      }
    }
    cout << "Case #" << cass << ": " << cont << endl;
  }
}