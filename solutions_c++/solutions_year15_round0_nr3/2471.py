#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;

#define pb push_back
#define pp pop_back
#define f first
#define s second
#define mp make_pair
#define sz(a) int((a).size())
#define fname "."

const int N = (int)1e5 + 123;
const double eps = 1e-6;
const int inf = (int)1e9 + 123;

using namespace std;

int l, x;
string a, b;

int id(char x) {
	if (x == 'i')
		return 2;
	if (x == 'j')
		return 3;
	return 4;
}

int to[5][5] = {0, 0, 0, 0, 0,
				0, 1, 2, 3, 4,
	            0, 2,-1, 4,-3,
	            0, 3,-4,-1, 2,
				0, 4, 3,-2,-1};

struct num {
	int x;
	num() {}
	num(int x) : x(x) {}
	num operator * (num b) {
		int res = to[abs(x)][abs(b.x)];
		if (x < 0)
			res *= -1;
		if (b.x < 0)
			res *= -1;					
		return res;
	}
};

num mult[N];
bool ok[N];

bool solve() {
    cin >> l >> x;
	cin >> a;
	b = "";
	while(x--)
		b += a;
	for (int i = 0; i < sz(b); i++) {
		if (i == 0)
			mult[i] = num(id(b[i]));
		else
			mult[i] = mult[i - 1] * num(id(b[i]));
	}
	memset(ok, 0, sizeof ok);
	for (int i = 1; i < sz(b); i++) {
		num now = num(1);
		for (int j = i; j > 0; j--) {
			now = num(id(b[j])) * now;
			if (mult[j - 1].x == 2 && now.x == 3) {
				ok[i] = 1;
				break;
			}
		}
	}
	bool ans = 0;
	num now = num(1);
	for (int i = sz(b) - 1; i > 1; i--) {
	    now = num(id(b[i])) * now;
		if (ok[i - 1] && now.x == 4) {
			ans = 1;
			break;
		}
	}
	return ans;
}

int t;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> t;
	for (int i = 1; i <= t; i++) {
		bool ans = solve();
		cout << "Case #" << i << ": ";
		if (ans)
			cout << "YES\n";
		else
			cout << "NO\n";
	}
	return 0;
}
