#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main (){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int z;
	cin >> z;
	for (int u = 0; u < z; ++u){
		ll k, c, s;
		cin >> k >> c >> s;
		ll odl = 1;
		for (int i = 0; i < c-1; ++i)
			odl *= k;
		ll x = 1;
		cout <<"Case #" << u+1 << ": ";
		for (int i = 0; i < s-1; ++i){
			cout <<x << ' ';
			x += odl;
		}
		cout << x;
		cout << '\n';
	}
}
