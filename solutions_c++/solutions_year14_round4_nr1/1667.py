#include <algorithm>
#include <bitset>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <typeinfo>
#include <utility>
#include <vector>
#include <complex>
#include <cmath>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef vector<int> vec;
typedef vector<vec> mat;
static const double EPS = 1e-9;
static const double PI = acos(-1.0);
const int INF = 1e9;
const int mod = 1e9 + 7;

int main(){
  int T;
  cin >> T;

  int N;
  int X;
  for(int t=1;t<=T;++t){
    cin >> N >> X;
    vector<int> s(X);
    for(int i=0;i<N;++i)cin >>s[i];

    sort(s.begin(),s.end());
    int cnt = N;

    int i=0;
    int j=N-1;
    for(int i=N-1;i>0;--i){
      for(int j=i-1;j>=0;--j){
	if(s[j]!=0 && )
      }
    }

    // answer
    cout << "Case #" << t << ": ";
    cout << cnt << endl;
  }
  return 0;
}
