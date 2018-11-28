#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define L(a) (int)((a).size())
#define all(a) (a).begin(), (a).end()
#define mp make_pair

#define Trace(X) cerr << #X << " = " << X << endl
#define _ << " - " << 

int main() {
	ios_base::sync_with_stdio(0);cin.tie(0);

	int n;
	string s;
	while (cin >> n) {
		int tc = 1;
		while (n-- && cin >> s) {
			int dif = 0;
			for (int i = 1; i < L(s); i++)
				if (s[i] != s[i-1])
					dif++;

			cout << "Case #" << tc++ << ": " << dif + (s.back() == '-') << endl;
		}
	}
    return 0;
}