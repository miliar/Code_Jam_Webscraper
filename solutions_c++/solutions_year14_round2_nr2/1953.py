#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>

#define F(i, n) for(i = 0;i < n; ++i)
#define pb(a, b) a.push_back(b)
#define lli long long int

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	lli t, cnt = 0, i, a, b, k, j;
	cin >> t;
	while(t--){
		lli ans = 0;
		cout << "Case #" << ++cnt << ": ";
		cin >> a >> b >> k;
		F(i, a){
			F(j, b){
				if((i & j) < k) ++ans; 
			}
		}
		cout << ans << "\n";
	}
	return 0;
}
