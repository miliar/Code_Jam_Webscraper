#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>

#define FOR(i, a, b) for (int i = (a);i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
using namespace std;

int field[100][100];

bool judge(int x,int y){
  bool yoko = true;
  bool tate = true;
  int debug = 0;
  REP(i,x)
    REP(j,y){
    yoko = true;tate = true;
    int cell = field[i][j];

    REP(k,x)/*yoko*/
      if (field[k][j] > cell)
	yoko = false;
    REP(t,y)/*tate*/
      if (field[i][t] > cell)
	tate = false;
    
    if (yoko == false && tate == false) 
      return false;
  }

  return true;
}

int main(){
  int N;
  int tate,yoko;
  bool ans[100];
  FILE* fp_in = freopen("B-large.in", "r", stdin);
  cin >> N;
  REP(k,N){
    cin >> tate >> yoko;
    REP(i,tate)
      REP(j,yoko)
      cin >> field[j][i];
    ans[k] = judge(yoko,tate);
  }
  
  REP(i,N){ 
     cout << "Case #"<< i+1 << ": ";
     if (ans[i])
       cout << "YES" << endl;
     else 
       cout << "NO" << endl;
  }
  
return 0;
}
