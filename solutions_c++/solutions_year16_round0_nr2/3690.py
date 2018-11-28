#include <bits/stdc++.h>

#define INF 0x3f3f3f3f
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define ForC(i, n) for (int i = 0; i < int(n); i++)
#define ForD(i, n) for (int i = int(n-1); i >= 0; i--)

using namespace std;
const double PI = acos(-1.0);

typedef long long ll;
typedef pair<int, int> pii;

int main (void) {
	int t;
	scanf("%d", &t);
	for (int cases = 1; cases <= t; cases++) {
		string str;
		cin >> str;
		int counter = 0;
		while (true) {
			bool flag = true;
			for (int i = 0; i < str.size(); i++) if (str[i] == '-') flag = false;
			if (flag) break;

			int k = 0;
			for (int i = 0; i < str.size(); i++) {
				if (str[i] == '+') {
					str[i] = '-';
					flag = true;
				} else break;
			}

			if (flag) counter++;
			flag = true;
			for (int i = 0; i < str.size(); i++) if (str[i] == '-') flag = false;
			if (flag) break;

			int j = 0;
			for (int i = str.size() - 1; i >= 0; i--) {
				if (str[i] == '-') {
					j = i;
					break;
				}
			}
			string aux = str;
			for (int i = 0; i <= j; i++) {
				str[i] = aux[j - i] == '-' ? '+' : '-';
			}
			counter++;
		}
		printf("Case #%d: %d\n", cases, counter);
	}
	return 0;
}
