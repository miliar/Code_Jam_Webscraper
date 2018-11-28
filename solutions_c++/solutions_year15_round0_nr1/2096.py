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
  ifstream fin("a.in");
  ofstream fout("a.out");
  fin >> T;
  REP(t, T){
    int smax;
    fin >> smax;
    string s;
    fin >> s;
    int ans=0;
    int sm=0;
    REP(i, len(s)){
      int n = s[i]-'0';
      if(n > 0 && sm < i){
        ans += i-sm;
        sm += i-sm;
      }
      sm += n;
    }
    fout << "Case #" << (t+1) << ": " << ans << endl;
  }
	return 0;
}
