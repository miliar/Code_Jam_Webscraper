#include<iostream>
#include<stdio.h>
#include<map>
#include<set>
#include<unordered_set>

using namespace std;

int main() {
	
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

	int t, tt = 0, y;
	long long n, c;
	cin >> t;
	
	while(t--) {
		tt++;
		cin >> n;
		cout << "Case #"<<tt<<": ";
		if(n == 0) cout << "INSOMNIA\n";
		else {
			set<int> store;
			y = 0;
			while(store.size() != 10) {
				y++;
				c = y * n;
				while(c) {
					store.insert(c % 10);
					c /= 10;
				}
			}
			cout << y * n << endl;
		}
	}
	return 0;
}
