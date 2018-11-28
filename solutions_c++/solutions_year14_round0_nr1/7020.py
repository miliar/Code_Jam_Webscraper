#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
using namespace std;

inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

int main() {
  int n;
  cin >> n;
  REP(i,n){
    int fa;
    cin >> fa;
    fa--;
    int fc[4][4];
    REP(r,4)REP(c,4)cin >> fc[r][c];
    int fb;
    cin >> fb;
    fb--;
    int fd[4][4];
    REP(r,4)REP(c,4)cin >> fd[r][c];
    int kc[4];
    REP(j,4)kc[j] = 0;
    REP(j,4)REP(k,4)if(fc[fa][j] == fd[fb][k])kc[j]++;
    int sum = 0;
    REP(j,4){
      sum+=kc[j];
    }
    if(sum==0){
      cout << "Case #"<<i+1<<": Volunteer cheated!\n";
    }else if(sum >1){
      cout << "Case #"<<i+1<<": Bad magician!\n";
    }else{
      cout << "Case #"<<i+1<<": ";
      REP(j,4)if(kc[j]!=0){
	cout << fc[fa][j] << endl;
      }
    }
  }


    return 0;
}
