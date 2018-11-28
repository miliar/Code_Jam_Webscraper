#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

struct node {
	string name;
	int price;
	bool operator < (const node & x) const {
		return price < x.price;
	}
} s[105], m[105], d[105];
int main() {
	ios_base::sync_with_stdio(false);
	int T, snum, mnum, dnum;
	cin >> T;
	while (T--) {
		cin >> snum >> mnum >> dnum;
		for (int i = 1; i <= snum; i++) {
			cin >> s[i].name >> s[i].price;
		}
		for (int i = 1; i <= mnum; i++) {
			cin >> m[i].name >> m[i].price;
		}
		for (int i = 1; i <= dnum; i++) {
			cin >> d[i].name >> d[i].price;
		}
		sort(s+1, s+1+snum);
		sort(m+1, m+1+mnum);
		sort(d+1, d+1+dnum);
		cout << s[snum/2+1].price+m[mnum/2+1].price+d[dnum/2+1].price << ' ' << s[snum/2+1].name << ' ' << m[mnum/2+1].name << ' ' << d[dnum/2+1].name << endl;
	}
}
