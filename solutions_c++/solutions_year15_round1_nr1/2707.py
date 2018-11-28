#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair
#define sf scanf
#define pf printf
#define N 1001
#define ms(x,y) memset(x, y, sizeof(x))
#define inf 1e9

int mush[N];
int n;

int DP[N];

int dp1(int i) {
	
	if (i >= n-1) return 0;
	if (DP[i] != -1)return DP[i];
	int ans = inf;
	ans = dp1(i+1) + mush[i];
	if (mush[i+1] >= mush[i]) ans = min(ans, dp1(i+1));		
	else {
		ans = min(ans, mush[i]-mush[i+1]+dp1(i+1));
	
	}
	return DP[i] = ans;	
}	


int main() {
	ios::sync_with_stdio(0);
	int t; cin >> t;
	for (int T = 1; T <= t; ++T) {
		 cin >> n;
		int y = 0, z = 0;
		cin >> mush[0];	
		for (int i = 1; i < n; ++i) {
			cin >> mush[i];
			//if (mush[i] < mush[i-1]) y += mush[i-1]-mush[i];
		}
		ms(DP, -1);
		y = dp1(0);
		//ms(DP, -1);
		//z = dp2(0);
		int speed = 0;
		int last = n-1;
		while (last) {
			if (mush[last] < mush[last-1]) speed = max(speed, mush[last-1]-mush[last]);
			--last;
		}
		
		for (int i = 0; i < n-1; ++i) {
			z += min(speed, mush[i]);
		}
		
		
		cout << "Case #" << T << ": ";
		cout << y  << ' ' << z;
		cout <<"\n";
	}
	
	return 0;
}
