#include <bits/stdc++.h>

using namespace std;

int main (int argc, char const *argv[]) {
	//freopen("input.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T, cs = 0, n; scanf("%d", &T); while(T--) {
		set <int> S;
		bool f = 1;
		scanf("%d", &n);
		cout << "Case #" << ++cs << ": ";
		for (int j = 1; j <= 100; j++) {
			int t = n * j;
			while (t) {
				S.insert(t%10);
				t/=10;
			}
			if (S.size()==10) {
				cout << n*j << endl;
				f = 0;
				break;
			}
		}
		if (f) cout << "INSOMNIA\n";
	}	
	return 0;
}

