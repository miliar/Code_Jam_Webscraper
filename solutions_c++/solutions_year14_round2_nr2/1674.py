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
  int A,B,K;
  for(int t=1;t<=T;++t){
    cin >> A >> B >> K;

    int cnt =0;
    for(int i=0;i<A;++i){
      for(int j=0;j<B;++j){
	//cout << (i&j) << endl;
	if( (i&j )< K)cnt++;
      }
    }

    cout << "Case #" << t << ": ";
    cout << cnt << endl;
  }
  return 0;
}
