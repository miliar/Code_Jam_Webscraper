
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

map<vector<long>, int> ans;
map<vector<long>, int> inq;

bool ok(vector<long> &f)
{
  if (f.size() <= 1) return true;
  
  
  int i = 1;
  for (;i < f.size();++i) {
    if (f[i - 1] > f[i]) {
      break;
    }
  }
  if (i == f.size()) return true;

  for (int j = i + 1;j < f.size();++j) {
    if (f[j] > f[j - 1]) {
      return false;
    }
  }
  return true;
}

//int search(vector<long> &f)
//{
//  if (ans.count(f) > 0) return ans[f];
//  cout<<ans.size()<<endl;
//  if (ok(f)) {
//    if (ans.count(f) == 0) {
//      ans[f] = 0;
//    }
//    return 0;
//  } else {
//    if (ans.count(f) > 0) {
//      return ans[f];
//    }
//    q[f] = 1;
//    int min = 10000000;
//    for (int i = 1;i < f.size();++i) {
//      swap(f[i], f[i - 1]);
//      if (q.count(f) == 0) {
//        int tmp = search(f) + 1;
//        if (tmp < min) {
//          min = tmp;
//        }
//      }
//      swap(f[i], f[i - 1]);
//    }
//    ans[f] = min;
//    return min;
//  }
//  return 0;
//}

void solve()
{
  int N;
  cin>>N;
  vector<long> f(N, 0);
  for (int i = 0;i < N;++i) {
    cin>>f[i];
  }
  ans.clear();
  inq.clear();
  
  queue<pair<int, vector<long> > > Q;
  inq[f] = 1;
  Q.push(make_pair(0, f));
  int min = 10000000;
  while (!Q.empty()) {
    pair<int, vector<long> > pr = Q.front();
    Q.pop();
    if (ok(pr.second)) {
      if (pr.first < min) {
        min = pr.first;
      }
    } else {
      for (int i = 1;i < pr.second.size();++i) {
        swap(pr.second[i], pr.second[i - 1]);
        if (inq.count(pr.second) == 0) {
          inq[pr.second] = 1;
          if (pr.first + 1 < min) {
            Q.push(make_pair(pr.first + 1, pr.second));
          }
        }
        swap(pr.second[i], pr.second[i - 1]);
      }
    }
  }
  cout<<min<<endl;
  
  //int result = search(f);
  //cout<<result<<endl;
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
