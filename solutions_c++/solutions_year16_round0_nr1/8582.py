#include <bits/stdc++.h>
using namespace std;
typedef long double ld;
typedef long long ll;
int digs(int x){
	if(x==0)
		return 0;
	int taken = 0;
	taken |= (1 << (x%10));
	return taken | (digs(x/10));
}
int solve(int x){
	int taken = 0, full = (1<<10)-1;
	for(int i = 1; ; ++i){
		taken|=digs(x*i);
		if(taken==full)
			return i;
	}
}
int main(){
	int n;
	cin >> n;
	for(int t = 1; t <= n; ++t){
		int x;
		cin >> x;
		cout << "Case #" << t << ": ";
		if(x==0)
			cout << "INSOMNIA\n";
		else
			cout << solve(x)*x << '\n';
	}
}

