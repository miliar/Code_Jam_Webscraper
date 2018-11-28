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
#include <cstring>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef vector<int> vec;
typedef vector<vec> mat;
static const double EPS = 1e-9;
static const double PI = acos(-1.0);

int m[4][4];

int main(){
  int T;
  cin >> T;
  int first,last;
  for(int t=1;t<=T;++t){
    map<int,int> mii;

    cin >> first;
    for(int i=0;i<4;++i)
      for(int j=0;j<4;++j)
	cin >> m[i][j];

    first--;
    for(int i=0;i<4;++i)
      mii[ m[first][i] ] = 1;

    cin >> last;
    for(int i=0;i<4;++i)
      for(int j=0;j<4;++j)
	cin >> m[i][j];

    last--;
    for(int i=0;i<4;++i)
      if( mii.count( m[last][i]   ))mii[ m[last][i]]++;
      else mii[ m[last][i]] = 1;

    vector<int> v;
    map<int,int>::iterator it = mii.begin(),end = mii.end();
    for(;it!=end;++it){
      if( it->second>=2) v.push_back(it->first);
    }
    cout << "Case #" << t << ": ";
    if(v.size()==1)
      cout << v[0] << endl;
    else if(v.size() >= 2)
      cout << "Bad magician!" << endl;
    else
      cout << "Volunteer cheated!" << endl;

  }
  return 0;
}
