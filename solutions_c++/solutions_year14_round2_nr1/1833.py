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

  string a,b;
  int N;
  for(int t=1;t<=T;++t){
    cin >> N;

    cin >> a >> b;

    int cnt=0;
    int i=0,j=0;
    bool flag = true;
    while( i < a.size() && j < b.size()){
      if(a[i] != b[j]){
	flag = false;
	break;
      }
      int at=0;
      int bt=0;
      while(j < b.size()-1 && a[i]==b[j+1]){
	j++;
	at++;
      }
      while(i < a.size()-1 && b[j]==a[i+1]){
	i++;
	bt++;
      }
      cnt += abs(at-bt);
      i++;j++;
    }
    if(a[i]!=b[j])flag = false;
    cout << "Case #" << t << ": ";
    if(flag==false)cout << "Fegla Won" << endl;
    else cout << cnt << endl;
  }
  return 0;
}
