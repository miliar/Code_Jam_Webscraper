#include<iostream>
#include<fstream>
using namespace std;
#define ll long long

int gcd(ll a, ll b){
	if (a < b) swap(a, b);
	if (b == 0)return a;
	return gcd(a%b, b);
}

int Solve(ll t, ll x , ll y)
{
	ll d = gcd(x, y); 
	x /= d; y/= d;
	
	ll deg = 1; for(int i = 1; i<=40; ++i) deg *= 2;
	ll cou = 0;
	if (deg % y != 0)return 0;
	x*= (deg/y);
	ll z = 1;
	while (2*z <= x){z*=2; ++cou;}
	return (40 - cou);
	
}

int main(){
	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	ll T;
	cin >> T;
	
	for(ll t  = 1; t<=T; ++t)
	{
		ll x, y; char c;
		cin >> x; cin >> c; cin >> y;
		ll d = Solve(t, x, y);
		cout << "Case #" << t << ": " ; if (d > 0) cout << d; else cout << "impossible"; cout << "\n";
	}
	return 0;
}
