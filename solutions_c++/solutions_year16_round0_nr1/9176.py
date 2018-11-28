#include<bits/stdc++.h>
using namespace std;
#define fileio freopen("in.txt","r",stdin); freopen("out.txt","w",stdout);
#define boost  ios_base::sync_with_stdio(false);


int main() {
	fileio;
	boost;
	int t, tt = 0, y;
	long long n, c;
	cin >> t;
	while(t--) {
		tt++;
		cin >> n;
		cout << "Case #"<<tt<<": ";
		set<int> digit;
		y = 0;
		while(digit.size() != 10 && y <= 1000000) {
			y++;
			c = y * n;
			while(c) {
				digit.insert(c % 10);
				c /= 10;
			}
		}
		if(digit.size() == 10) cout << y * n << endl;
		else cout << "INSOMNIA\n";
	}
	return 0;
}
