#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>

#define oo 1e9
#define pi 3.1415926536
#define all(x) x.begin(),x.end()
#define sorta(x) sort(all(x))
#define sortam(x,comp) sort(all(x),comp)
#define sortd(x) sort(x.rbegin(),x.rend())
#define pb push_back
#define mp make_pair
#define sf(x) scanf("%d", &x);
#define sfll(x) scanf("%I64d", &x);
#define pr(x) printf("%d ", x);

typedef long long ll;
using namespace std;

string mul(string a, char b) {
	string ret;
	if(a[0] == '-') ret += '-', a.erase(0, 1);

	if(a + b == "1i") ret += "i";
	if(a + b == "1j") ret += "j";
	if(a + b == "1k") ret += "k";
	if(a + b == "ii") ret += "-1";
	if(a + b == "ij") ret += "k";
	if(a + b == "ik") ret += "-j";
	if(a + b == "ji") ret += "-k";
	if(a + b == "jj") ret += "-1";
	if(a + b == "jk") ret += "i";
	if(a + b == "ki") ret += "j";
	if(a + b == "kj") ret += "-i";
	if(a + b == "kk") ret += "-1";

	if(ret.size() == 3) ret.erase(0, 2);
	return ret;
}

string mul2(char a, string b) {
	string ret;
	if(b[0] == '-') ret += '-', b.erase(0, 1);

	if(a + b == "i1") ret += "i";
	if(a + b == "j1") ret += "j";
	if(a + b == "k1") ret += "k";
	if(a + b == "ii") ret += "-1";
	if(a + b == "ij") ret += "k";
	if(a + b == "ik") ret += "-j";
	if(a + b == "ji") ret += "-k";
	if(a + b == "jj") ret += "-1";
	if(a + b == "jk") ret += "i";
	if(a + b == "ki") ret += "j";
	if(a + b == "kj") ret += "-i";
	if(a + b == "kk") ret += "-1";

	if(ret.size() == 3) ret.erase(0, 2);
	return ret;
}


int main() {
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	sf(t);
	for(int tc = 1; tc <= t; tc++) {
		printf("Case #%d: ", tc);
		int l, x;
		string s;
		cin >> l >> x >> s;

		bool ok = 1;
		int mini = l*x + 2, maxk = -1;
		string tmp = "1";
		for(int i = 0; i < l*x; i++) {
			tmp = mul(tmp, s[i%l]);
			if(tmp == "i") mini = min(mini, i);
		}
		ok &= (tmp == "-1");
		
		tmp = "1";
		for(int i = l*x - 1; i >= 0; i--) {
			tmp = mul2(s[i%l], tmp);
			if(tmp == "k") maxk = max(maxk, i);
		}
		ok &= (mini < maxk);

		ok ? cout << "YES\n" : cout << "NO\n";
	}
	return 0;
}
