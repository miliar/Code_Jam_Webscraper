#include <bits/stdc++.h>

using namespace std;


int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	long long t, m, res, sum;
	string str;
	cin >> t;
	for(int idx = 1; idx <= t; ++idx) {
	  res = sum = 0;
	  cin >> m >> str;
	  for(int i = 0; i <= m; ++i) {
	    if(i > sum && str[i] != '0') res += i - sum, sum += i - sum;
	    sum += (str[i] - '0');
	  }
	  printf("Case #%d: %lld\n", idx, res);
	}
  return 0;
}
