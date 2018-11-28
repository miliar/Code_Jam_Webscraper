
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
    string s;
    int k;
    cin>>s>>k;
    int cnt = 0;
    for (int i = 0;i < s.size();++i) {
      int start = i;
      int end = i + k - 1;
      if (end >= s.size()) break;
      if (s[i] == '-') {
        cnt += 1;
        for (int j = start;j <= end;++j) {
          if (s[j] == '-') s[j] = '+';
          else s[j] = '-';
        }
      }
    }
    int find = 0;
    for (int i = 0;i < s.size();++i) {
      if (s[i] == '-') find = 1;
    }
    if (find) cout<<"IMPOSSIBLE"<<endl;
    else cout<<cnt<<endl;
		//break;
  }
	return 0;
}
