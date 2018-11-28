#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <string>
#include <sstream>
typedef long long ll;
using namespace std;

#define FORi(n) for(int i=0;i<n;++i)
#define FOR(i,a,b) for(int i=a;i<=b;++i)
#define mp make_pair
#define pb push_back
#define sz(x) int((x).size())

string inttostr (int a) {
    string s;
    ostringstream os;
    os << a;
    s = os.str();
    return s;
}

ll p[16];
int* num;
int* num2;

bool isPoly (int* a, int dim) {
	bool res = true;
	int l = 0, r = dim;
	while (a[l]==0) l++;
	while (l < r) {
		if (a[l++] != a[r--]) res = false;		
	}
	return res;
}

void inc(int* a) {
	int k = 7;
	a[k]++;
	while (a[k] >= 10) {
		a[k] = 0;
		k--;
		a[k]++;
	};
}

ll toNum (int* a) {
	ll r = 0;
	for (int i = 7; i >= 0; --i)
		r += a[i]*p[7-i];
	r *= r;
	return r;
}

bool bCheck (ll a) {
	for (int i = 15; i >= 0; --i)
		num2[i] = a / p[15-i] % 10;
	if (isPoly(num2, 15)) return true;
	return false;
}

void solve () {
	num  = new int[8];
	num2 = new int[16];
	vector<ll> ans;
	ll res = 0;
	
	FORi(8) num[i] = 0;
	p[0] = 1;
	FOR(i,1,15) p[i] = p[i-1]*10;

	while (num[0] <= 5) {
		inc(num);
		if (isPoly(num, 7)) {
			res = toNum(num);
			if (bCheck(res))
				ans.pb(res);
		}
	}

	int T = 0;
	cin >> T;
	for (int test_id = 1; test_id <= T; test_id++) {
		ll A, B;
		cin >> A >> B;
		int res = 0;
		for (int i = 0; i < ans.size(); ++i)
			if (ans[i] >= A && ans[i] <= B) res++;
		cout << "Case #" << test_id << ": " << res << endl;
	}
}

void main()
{
    #ifdef _DEBUG
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif

    solve();
}