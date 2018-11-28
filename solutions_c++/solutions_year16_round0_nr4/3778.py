#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;
typedef long long LL;
void main(){
	
	freopen("fractal.in", "r", stdin);
    freopen("fractal.out", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    int T; cin >> T;
	int k,c,s;
	for (int t = 1; t <= T; t++){
		cin >> k >> c >> s;
		cout << "Case #" << t << ": ";
		if (k==1) {
			cout << 1 << endl;
			continue;
		}
		else if (c == 1){
			if (s < k) cout << "IMPOSSIBLE" << endl;
			else{
			for(int i=1; i < k ; i++){
				cout << i << " ";
			}
			cout << k << endl;
			}
		}
		else {
			if (s < k-1) cout << "IMPOSSIBLE" << endl;
			else{
			for(int i=2; i < k ; i++){
				cout << i << " ";
			}
			cout << k << endl;
			}
		}
		//cout << "" << endl;
	}
}