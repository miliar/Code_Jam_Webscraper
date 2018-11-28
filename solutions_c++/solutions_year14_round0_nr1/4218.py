#include <bits/stdc++.h>
using namespace std;

#define oo 1LL<<30
#define SZ(x) ((int)x.size())
#define valid(x,u) (x>=0 && x<u)
#define endl '\n'

int di [] = {0, 0, 1, -1, 1, 1, -1, -1};
int dj [] = {1, -1, 0, 0, 1, -1, 1, -1};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	freopen("in.in", "rt", stdin);
	freopen("out.out", "wt", stdout);

	int T, id = 0;
	cin >> T;

	while(T --) {
		set <int> s1, s2;
		int n, a;
		cin >> n; n --;
		for(int i=0; i<4; i++)
		for(int j=0; j<4; j++) {
			cin >> a;
			if(i == n) s1.insert(a);
		}
		cin >> n; n --;
		for(int i=0; i<4; i++)
		for(int j=0; j<4; j++) {
			cin >> a;
			if(i == n && s1.count(a))
				s2.insert(a);
		}
		cout << "Case #" << ++id << ": ";
		if(SZ(s2) == 1) {
			cout << *s2.begin() << endl;
		} else if(s2.empty()) {
			cout << "Volunteer cheated!" << endl;
		} else {
			cout << "Bad magician!" << endl;
		}
	}

	return 0;
}
