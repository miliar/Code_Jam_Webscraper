
#include <assert.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>

using namespace std;
void solve()
{
  int N, X;
  cin>>N>>X;
  vector<int> f(N, 0);
  for (int i = 0;i < N;++i) {
    cin>>f[i];
  }
  sort(f.begin(), f.end(), greater<int>());
  vector<int> mark(N, 0);
  int cnt = 0;
  for (int i = 0;i < N;++i) {
    if (mark[i]) continue;
    mark[i] = 1;
    cnt += 1;
    for (int j = i;j < N;++j) {
      if (!mark[j]) {
        if (f[j] + f[i] <= X) {
          mark[j] = 1;
          break;
        }
      }
    }
  }
  cout<<cnt<<endl;
}
int main()
{
  //freopen("data.txt", "r", stdin);
  freopen("/home/zhanyi/Downloads/A-small-attempt0.in", "r", stdin);
	//freopen("A-small-practice.in", "r", stdin);
	//freopen("A-large-practice.in", "r", stdin);
  //freopen("ans.txt", "w", stdout);
  int t;
  cin>>t;
  for (int i = 1;i <= t;++i) {
    cout<<"Case #"<<i<<": ";
    solve();
		//break;
  }
	return 0;
}
