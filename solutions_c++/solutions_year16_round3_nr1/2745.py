#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>

#define F first
#define S second

using namespace std;

void solve() {
	int n;
	pair<int, int> p[30];
	cin >> n;
	int sum = 0;
	for(int i = 1; i <= n; ++i) {
		p[i].S = i;
		cin >> p[i].F;
		sum += p[i].F;
	}
	sort(p + 1, p + n + 1, greater<pair<int, int> >());
	if(sum & 1) {
		p[1].F--;
		cout << (char) (p[1].S + 'A' - 1) << " ";
		sort(p + 1, p + n + 1, greater<pair<int, int> >());
	}
	do {
		
		if(p[1].F > 0) {
			p[1].F--;
			cout << (char) (p[1].S + 'A' - 1);
		}
		if(p[2].F > 0) {
			p[2].F--;
			cout << (char) (p[2].S + 'A' - 1);
		}
		cout << ' ';
		sort(p + 1, p + n + 1, greater<pair<int, int> >());
	}while(p[1].F > 0);

}

int main() {
	freopen("input.txt", "r", stdin);
	int t;
	cin >> t;
	for(int iter = 1; iter <= t; ++iter){
		cout << "Case #" << iter << ": ";
		solve();
		cout << '\n';
	}
}