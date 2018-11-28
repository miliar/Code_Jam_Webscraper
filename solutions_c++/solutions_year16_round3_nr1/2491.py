#include <bits/stdc++.h>

#define pb push_back
#define endl "\n"

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " " <<

using namespace std;

int n;
int ns[30];
int total;
int test;

void drop(int i) {
	char p = 'A'+i;
	cout << p << ' ';
	ns[i]--;
	total--;
}

void drop2(int i, int j) {
	char p1 = 'A'+i;
	char p2 = 'A'+j;
	cout << p1 << p2 << ' ';
	ns[i]--; ns[j]--;
	total -= 2;
}

void check() {
	REP(i,n) {
		if(ns[i] > total/2) {
			cerr << "TEST " << test << " FAUX " << i << endl;
		}
	}
}

int main() {
	ios_base::sync_with_stdio(0);

	int nTests;
	cin >> nTests;
	for(test = 1; test <= nTests; test++) {
		cout << "Case #" << test << ": ";
		cin >> n;
		total = 0;
		REP(i, n) {
			cin >> ns[i];
			total += ns[i];
		}

		while(total > 0) {
			int max1=0,max2=1;
			int nNotEmpty = 0;
			REP(i,n) {
				if(ns[i] > 0) nNotEmpty++;
				if(ns[i] > ns[max1]) {
					max2 = max1;
					max1 = i;
				}
				else if(ns[i] > ns[max2]) {
					max2 = i;
				}
			}

			if(ns[max1] == ns[max2] && nNotEmpty > 2) {
				drop(max1);
			}
			else {
				drop2(max1,max2);
			}
			check();
		}
		


		cout << endl;
	}

	return 0;
}
