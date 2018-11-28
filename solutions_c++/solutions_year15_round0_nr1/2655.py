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

#pragma comment(linker, "/STACK:133217728")

using namespace std;

int solve(string s) {
	int res = 0;
	int cur = s[0] - '0';

	for(int i=1; i<s.length(); i++) {
		if(cur < i) {
			res += i - cur;
			cur = i;
		}
		cur += s[i] - '0';
	}
	return res;
}
int main() {  
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    int T;
	cin >> T;

	for(int t=1; t<=T; t++) {
		int n;
		string s;
		cin >> n >> s;

		cout << "Case #" << t << ": " << solve(s) << endl;

	}
    return 0;
}