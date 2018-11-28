#include <vector>
#include <list>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <limits>
#include <tuple>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iterator>
#include <string>
#include <fstream>
#define REP(k,a) for(int k=0; k < (a); ++k)
#define REPP(k,a,b) for(int k= (a); k < (b); ++k)
#define INF 200000000
#define mp make_pair
#define len(s) (int)((s).size())
#define pb push_back

using namespace std;
typedef long long ll;
typedef unsigned int uint;
using vi = vector<int>;
using vii = vector<vector<int>>;
using pii = pair<int,int>;
template <class T>
void print(vector<T> v){ bool first=true; for(T x : v) { if(!first) cout << " "; first = false; cout << x; } cout << endl;}

int main(){
  int T;
  ifstream fin("b.in");
  ofstream fout("b.out");
  fin >> T;

  REP(t, T){
    int d;
    fin >> d;
    vi v(d);
    int m=0;
    REP(i, d){
      int n;
      fin >> n;
      v[i] = n;
      m = max(n, m);
    }
    int ans=m;
    REPP(i, 2, m+1){
      int curr=i;
      REP(j, d){
        int d1=v[j]/i;
        if(v[j] % i == 0) d1--;
        curr += d1;
      }
      ans = min(ans, curr);
    }
    fout << "Case #" << (t+1) << ": " << ans << endl;
  }
	return 0;
}
