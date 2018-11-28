#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

main() {
	FILE *fin = freopen("A-large.in", "r", stdin);
	FILE *fout = freopen("A-large.out", "w", stdout);
	assert( fin!=NULL );
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		LL n;
		cin >> n;
		if(n == 0){
			cout << "INSOMNIA" << endl;
			continue;
		}
		set<int> p;
		for(int c = 0; c < 10; c++) p.insert(c);
		for(LL i = 1; i < 10000; i++){
			LL d = n*i;
			while(d > 0){
				p.erase(d%10);
				d /= 10;
			}
			if(p.size() == 0){
				cout << n*i << endl;
				break;
			}
		}

	}
	exit(0);
}