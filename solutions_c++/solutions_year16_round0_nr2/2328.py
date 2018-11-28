#include<iostream>
#include<iomanip>
#include<queue>
#include<stack>
#include<sstream>
#include<algorithm>
#include<list>
#include<map>
#include<vector>
#include<string>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<set>

#define Author "DemoVersion"
#define DBG(x) cout<<#x<<" = "<<x<<";\n"


using namespace std;
int dx[] = { 0,0,-1,1,1,-1,1,-1 };
int dy[] = { 1,-1,0,0,1,1,-1,-1 };
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;

/// Hey yo man, lets do some contest!

int solve(string str) {
	int i,ret=0;
	for (i = 0;i + 1 < str.length();i++) {
		if (str[i] != str[i + 1])ret++;
	}
	if (str[i] == '-')ret++;
	return ret;
}
int main() {
	int test, t;
	cin >> t;
	string str;
	for (test = 1;test <= t;test++) {
		cin >> str;
		cout << "Case #" << test << ": "<<solve(str)<<"\n";
	}
	return 0;
}
