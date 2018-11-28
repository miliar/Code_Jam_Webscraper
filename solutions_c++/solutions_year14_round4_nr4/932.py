
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

int m, n;
long long num;
long long MAX;
vector<string> s;
int tire(vector<int> &id)
{
  //return 1;
  map<string, int> sm;
  for (int i = 0;i < id.size();++i) {
    for (int j = 0;j < s[id[i]].size();++j) {
      //for (int k = j;k < s[id[i]].size();++k) {
        //string tmp(s[id[i]].begin() + j, s[id[i]].begin() + k + 1);
        string tmp(s[id[i]].begin(), s[id[i]].begin() + j + 1);
        if (sm.count(tmp) == 0) {
          sm[tmp] = 1;
        }
      //}
    }
  }
  return sm.size() + 1;
}

void search(int i, vector<int> &wh)
{
  if (i >= m) {
    map<int, vector<int> > mp;
    for (int j = 0;j < wh.size();++j) {
      if (mp.count(wh[j]) == 0) {
        mp[wh[j]] = vector<int>();
      }
      mp[wh[j]].push_back(j);
    }
    if (mp.size() == n) {
      int sum = 0;
      for (int j = 0;j < n;++j) {
        int cnt = tire(mp[j]);
        sum += cnt;
      }
      if (MAX == -1) {
        MAX = sum;
        num = 1;
      } else if (sum == MAX) {
        num = (num + 1) % 1000000007;
      } else if (sum > MAX) {
        MAX = sum;
        num = 1;
      }
    }
  } else {
    for (int j = 0;j < n;++j) {
      wh[i] = j;
      search(i + 1, wh);
    }
  }
}

void solve()
{
  s.clear();
  cin>>m>>n;
  for (int i = 0;i < m;++i) {
    string tmp;
    cin>>tmp;
    s.push_back(tmp);
  }
  MAX = -1;
  num = 0;

  
  vector<int> wh(m, 0);
  search(0, wh);
  cout<<MAX<<' '<<num % 1000000007<<endl;
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
