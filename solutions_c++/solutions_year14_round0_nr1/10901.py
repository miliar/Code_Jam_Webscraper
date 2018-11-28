#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <array>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <string>
#include <algorithm>
#include <numeric>
#include <utility>
#include <cstdlib>
#include <ctime>
#include <cstdint>
#include <cmath>

#define FOR(i,k,n)  for(int i = (k);i < (n);++i)
#define REP(i,n)    FOR(i,0,n)
#define EACH(i,x)   for(auto & i : x)
#define ALL(x)      begin(x),end(x)

using namespace std;

typedef vector<int> vecint;

int main()
{
  int T;
  cin>>T;
  REP(i,T) {
    cout << "Case #" << (i+1) << ": ";
    int r[2];
    int tb[2][4][4];
    REP(j,2){
      cin>>r[j];
      r[j]--;
      REP(k,4){
        REP(l,4){
          cin>>tb[j][k][l];
        }
      }
    }
    vecint maybe;
    REP(j,16){
      bool ok[2] = {false,false};
      REP(k,4){
        REP(l,2){
          if(tb[l][r[l]][k] == (j+1)){
            ok[l]=true;
          }
        }
      }
      if(ok[0]&&ok[1])
        maybe.push_back(j);
    }
    switch(maybe.size()){
      case 0:
      cout << "Volunteer cheated!" << endl;
      break;
      case 1:
      cout << (maybe[0]+1) << endl;
      break;
      default:
      cout << "Bad magician!" << endl;
    }
  }
  return 0;
}
