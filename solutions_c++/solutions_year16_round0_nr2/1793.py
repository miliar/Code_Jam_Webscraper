#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <stdexcept>
#include <functional>
#include <math.h>
#include <utility>
#include <sstream>
#pragma comment(linker, "/STACK:133217728")

using namespace std;
int cnt[47];
int c = 0;

void f(int n) {
	while(n > 0) {
		int p = n % 10;
		n /= 10;
		if(++cnt[p] == 1) c++;
	}
}
int main() {  
	freopen("in.txt", "r", stdin);
	freopen("ans.txt", "w", stdout);
	int T;
	cin >> T;
	for(int t=1; t<=T; t++) {
		string s;
		cin >> s;
		int ans = 0;
		int plus = 0;
		for(int i=0; i<s.length(); i++) {
			if(i && s[i] == s[i-1]) continue;
			if(s[i] == '-') {
				ans += 1 + plus;
			}
			plus = 1;
		}
		cout << "Case #" << t << ": ";
		cout << ans << endl;
	}
	return 0;
}