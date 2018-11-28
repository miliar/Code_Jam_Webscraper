#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <stack>
#include <queue>
#include <cmath>
#include <fstream>
#include <functional>
#include <iomanip>

using namespace std;

#define PI acos(-1)
#define CNT PI/180
#define INF 99999999
const double EPS = 1e-10;
typedef vector<vector<pair<int, int> > > graph;

int main (){

	ios::sync_with_stdio(false);
	
	int t;
  cin >> t;
  int Case = 1;
  while (t--){
    int n;
    string s;
    cin >> n >> s;

    int up = (int)s[0] - 48;
    int ans = 0;

    for (int i=1; i<s.size(); i++){
      int num = (int)s[i] - 48;
      if ( up < i  ){
        ans += i-up;
        up +=  i-up;
      }
      up += num;
    }
    cout << "Case #" << Case++ << ": " << ans << endl;
  }

	

	return 0;
}
