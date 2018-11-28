#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<algorithm>
#include<sstream>
#include<limits.h>
#include<iomanip>
#include<cstring>
#include<bitset>
#include<fstream>
#include<cmath>
#include<cassert>
#include <stdio.h>
#include<ctype.h>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, n; cin >> T;
	string str;
	for(int t = 1; t <= T; ++ t) {
		cin >> n >> str;
		for(int i = 0; i <= n; ++ i) str[i] -= '0';
		int res = 0;
		int curr = 0;
		for(int i = 0; i <= n; ++ i) {
			if(i > curr && str[i]) {
				res += i - curr;
				curr = i;
			}
			curr += str[i];
		}
		printf("Case #%d: %d\n", t, res);
	}
}