#include <bits/stdc++.h>
using namespace std;

int main(){

	int t;
	int n, lim;
	cin >> t >> n >> lim;

	cout << "Case #1:" << endl;

	for(long long mask = 0, cnt = 0; mask < (1<<n) && cnt < lim; mask++){
		if( (mask & 1) && (mask & (1<<(n-1))) ){
			bool good = true;
			vector<long long> ans(11);
			for(long long b = 2; good && b < 11; b++){
				long long a = 0, p = 1;
				for(int i = 0; i < 16; i++){
					if( (mask & (1<<i)) )
						a += p;
					p *= b;
				}
				good = false;
				for(long long i = 2; i*i <= a; i++){
					if(a % i == 0){
						good = true;
						ans[b] = i;
						break;
					}
				}
			}
			if(good){
				for(int i = n-1; i >= 0; i--)
					if( (mask & (1<<i)) )
						cout << 1;
					else
						cout << 0;
				cout << " ";
				for(int b = 2; b < 11; b++)
					cout << ans[b] << " ";
				cout << endl;
				cnt++;
			}
		}
	}

	return 0;
}
