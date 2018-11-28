#include <bits/stdc++.h>
using namespace std;

int mark(int x) {
	if(x == 0)
		return 1;
	int res = 0;
	while(x != 0) {
		res |= (1<<(x%10));
		x /= 10;
	}
	return res;
}

bool all(int x) {
	return (x == ((1<<10)-1));
}

int main () {
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		int n, i = 1;
		cin >> n;
		int cover = 0;
		while(i < 10000) {
			cover |= mark(n*i);
			if(all(cover)) {
				cout << (n*i) << endl;
				break;
			}
			i++;
		}
		if(!all(cover))
			cout << "INSOMNIA" << endl;
	}
	return 0;
}
