#include <bits/stdc++.h>
using namespace std;
int t, n, j, x[17];
int main(){
	ios :: sync_with_stdio(false);
	freopen("gcj.in", "r", stdin);
	freopen("gcj.out", "w", stdout);
	cin >> t;
	x[1] = x[16] = 1;
	for(int qq = 1; qq <= t; qq++){
		cout << "Case #" << qq << ":\n" ;
		cin >> n >> j;
		for(int i = 0 ; i < 500; i++){
			int idx = 15, temp = i;
			while(temp){
				x[idx--] = temp & 1;
				temp >>= 1;
			}
			for(int k = 1; k <= 16; k++) cout << x[k] << x[k];
			for(int k = 2; k <= 10; k++) cout << " " << (k + 1);
			cout << '\n';
		}
	}
}