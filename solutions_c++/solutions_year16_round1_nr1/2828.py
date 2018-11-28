#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mk make_pair
#define fi first
#define se second

typedef unsigned long long ull;
typedef unsigned int ui;
typedef long long ll;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);

const int N = 3e3; 
const int MID = 1500;
string s;
char res[N];

void go() {
	int i = MID, j = MID;
	memset(res, 0, sizeof res);

	res[i] = s[0];
	for (int k = 1; k < s.size(); k++) {
		if (s[k] >= res[i]) {
			res[--i] = s[k];
		} else {
			res[++j] = s[k];
		}
	}

}

void printres() {
	for (int i = 0; i < N; i++) {
		if (res[i] != 0)  cout << res[i];
	}	cout << endl;
}

int main (void) {
	ios_base::sync_with_stdio(false);

	int t;	cin >> t;
	for (int T = 1; T <= t; T++) {
		cout << "Case #" << T << ": ";
		cin >> s;
		go ();
		printres();
	}


	return 0;
}
