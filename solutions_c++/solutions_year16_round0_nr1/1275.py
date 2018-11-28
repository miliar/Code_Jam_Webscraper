#include <bits/stdc++.h>
using namespace std;
int t, mul, f[10], distinct;
long long n;
int main(){
	ios :: sync_with_stdio(false);
	freopen("gcj.in", "r", stdin);
	freopen("gcj.out", "w", stdout);
	cin >> t;
	for(int qq = 1; qq <= t; qq++){
		cout << "Case #" << qq << ": ";
		cin >> n;
		if(n == 0){ 
			cout << "INSOMNIA\n";
			continue;
		}
		memset(f, 0, sizeof f);
		distinct = mul = 0;
		while(true){
			++mul;
			long long temp = n * mul;
			while(temp){
				if(!f[temp % 10]) distinct++, f[temp % 10]++;
				temp /= 10;
			}
			if(distinct == 10){
				cout << (n * mul) << '\n';
				break;
			}
		}
	}
}