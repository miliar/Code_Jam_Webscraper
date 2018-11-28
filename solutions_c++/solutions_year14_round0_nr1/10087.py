//Bakuri Tsutskhashvili

#define _CRT_SECURE_NO_DEPRECATE

# include <cmath>
# include <cstdio>
# include <vector>
# include <bitset>
# include <iostream>
# include <algorithm>
# include <string>
# include <set>
# include <map>

# define ll long long
# define INF 100000000
# define fesvi(popo) sqrt(double(popo))
# define Pi acos(-1.0)
# define MAX(a,b) (a>b?a:b)
# define MIN(a,b) (a<b?a:b)
# define md 1000000007

using namespace std;
ll t;
int main(){
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);   freopen("output.txt", "w", stdout);
#endif
	scanf("%lld", &t);
	ll cas = 1;
	while (t--){
		ll ans1, ans2;
		vector<ll> a(17, 0);
		ll x;
		scanf("%lld", &ans1);
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++){
				scanf("%lld", &x);
				if (i == ans1)
					a[x]++;
			}
		scanf("%lld", &ans2);
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++){
				scanf("%lld", &x);
				if (i == ans2)
					a[x]++;
			}
		cout << "Case #" << cas << ": ";
		ll s = 0;
		ll f;
		for (int i = 1; i <= 16; i++)
			if (a[i] == 2)
				s++, f = i;
		if (s == 0)
			cout << "Volunteer cheated!";
		if (s == 1)
			cout << f;
		if (s > 1)
			cout << "Bad magician!";
		cout << "\n";
		cas++;
	}
}