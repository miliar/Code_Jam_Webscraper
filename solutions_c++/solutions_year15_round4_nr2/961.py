//In the name of God
#include <bits/stdc++.h>
using namespace std;
typedef long double ld;
ofstream fout("GCJB.out");
#define cout fout
int main(){
	int tc;
	cin >> tc;
	int ts = 1;
	while(tc--){
		cout << "Case #" << ts++ << ": ";
		int n;
		cin >> n;
		ld r1,c1,r2,c2;
		ld v,c;
		if(n == 1){
			cin >> v >> c >> r1 >> c1;
			if(c != c1){
				cout << "IMPOSSIBLE\n";
				continue;
			}
			cout << setprecision(10) << fixed << v / r1 << '\n';
			continue;
		}
		cin >> v >> c;
		cin >> r1 >> c1 >> r2 >> c2;
		if(c > c1 && c > c2 || c < c1 && c < c2){
			cout << "IMPOSSIBLE\n";
			continue;
		}
		if(c1 == c2){
			cout << setprecision(10) << fixed << v / (r1 + r2)<< '\n';
			continue;
		}
		c -= c1;
		c2 -= c1;
		ld v2 = v * c / c2;
		cout << setprecision(10) << fixed << max(v2 / r2, (v - v2) / r1) << '\n';
		
	}
	return 0;
}
