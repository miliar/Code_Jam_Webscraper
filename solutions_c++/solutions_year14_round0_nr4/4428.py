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

template< class Iterator>
void print(Iterator first,Iterator last){
  while(first != last){
    cout << *first++ << " ";
  }cout << endl;
}
int main(){
  int T;
  cin >> T;

  int N;
  for(int t=1;t<=T;++t){
    cin >> N;
    int max_ans = 0;
    int min_ans = N;
    vector<double> pre(N),aft(N);
    for(int i=0;i<N;++i) cin >> pre[i];
    for(int i=0;i<N;++i) cin >> aft[i];

    sort(pre.begin(),pre.end());
    do{
      //print(pre.begin(),pre.end());
      int maxtmp = 0,mintmp = N;
      for(int i=0;i<N;++i){
	maxtmp += (pre[i] > aft[i]);
      }
      max_ans = max(max_ans, maxtmp);
      min_ans = min(min_ans, maxtmp);

    } while(next_permutation(pre.begin(),pre.end()));

    cout << "Case #" << t << ": " << max_ans << " " << min_ans << endl;
  }

  return 0;
}
