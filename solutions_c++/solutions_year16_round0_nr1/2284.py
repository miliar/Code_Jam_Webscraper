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

bool check(int add, int n, char inpt[]) {
	int i, ac;
	ac = inpt[0] - '0' + add;
	for (i = 1;i <= n;i++) {
		if (ac < i)return 0;
		ac += inpt[i] - '0';
	}
	return 1;
}
int btmsk;
void add(int num) {
	int it;
	while (num > 0) {
		it = num % 10;
		btmsk |= (1 << it);
		num /= 10;
	}
}
int solve(int n) {
	int i;
	btmsk = 0;
	for (i = 1;;i++) {
		add(n*i);
		if (btmsk == ((1 << 10) - 1))break;
	}
	return n*i;
}
int main() {
	int n, test, t;
	cin >> t;
	
	for (test = 1;test <= t;test++) {
		cin >> n;
		cout << "Case #" << test << ": ";
		if (n) {
			cout << solve(n);
		}else {
			cout << "INSOMNIA";
		}
		cout << "\n";
	}
	return 0;
}
