#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <utility>
#include <vector>
#include <iterator>
#include <map>
#include <set>
#include <algorithm>
#include <list>

#define FOR(i,n) for(int i = 0, n_ = (n); i<n_; i++)
#define ITER(it, lst) for(typeof((lst).begin()) it = (lst).begin(); it != (lst).end(); ++it)
#define N 4

using namespace std;

inline void updatemax(int &a, int b) { if(a<b) a = b; }
inline void updatemin(int &a, int b) { if(a>b) a = b; }

int main(){
  int T;
  cin >> T;

  FOR(t, T){
    int m, n, h;
    cin>>n>>m;
    
    vector< vector<int> > lawn(n);
    vector<int> maxrow(n, 0), maxcol(m, 0);

    FOR(i, n){
      lawn[i] = vector<int>(m);
      FOR(j, m) {
	cin >> h;
	lawn[i][j] = h;
	updatemax(maxrow[i],h);
	updatemax(maxcol[j],h);
      }
    }

    bool feasible = true;
    FOR(i, n){
      FOR(j, m) 
	if(lawn[i][j] != min(maxrow[i], maxcol[j])){
	  feasible = false;
	  break;
	}
      if(!feasible) break;
    }
    cout<<"Case #"<<t+1<<": "<<(feasible?"YES":"NO")<<endl;
  }
  return 0;
}
