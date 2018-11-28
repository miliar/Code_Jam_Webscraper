#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <set>
#include <stack>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

const int NMAX = 100000 + 7;
const int INF = 1000000000;

int cnt = 50;

ll convert(const string &s,int base) {
	ll ans = 0;
	for (int i=0;i<s.length();i++) {
		ans *= base;
		ans += s[i] - '0';
	}
	return ans;
}

ll smallestDivisor(ll x) {
	if (1==x) {
		return -1;
	}
	for (int i=2;i*1ll*i<=x;i++) {
		if (x%i ==0) {
			return i;
		}
	}
	return -1;
}

void go(string &pref, int len) {
	if (cnt <= 0){
		return ;
	}
	if (1==len) {
		pref.push_back('1');
		bool ok = true;
		ll ans[11] = {0};
		for (int i=2;i<=10;i++) {
			ll num = convert(pref,i);
			ll divisor = smallestDivisor(num);
			if (divisor == -1) {
				ok = false;
				break;
			}
			ans[i] = divisor;
		}
		if (ok) {
			cnt--;
			cout << pref;
			for (int i=2;i<=10;i++) {
				cout << " " << ans[i];
			}
			cout << endl;
		}
		pref.pop_back();
		return ;
	}
	pref.push_back('0');
	go(pref,len-1);
	pref.pop_back();
	pref.push_back('1');
	go(pref,len-1);
	pref.pop_back();
}

int main() {
	freopen("input.txt","r",stdin);
	// freopen("output.txt","w",stdout);
	int t;
	int len;
	cin >> t;
	cin >> len;
	cin >> cnt;
	string s="1";
	cout << "Case #1: " << endl;
	go(s,len - 1);

	return 0;
}