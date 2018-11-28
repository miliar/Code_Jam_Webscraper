#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define mp make_pair
#define pb push_back

#define MOD 1000000007LL

void solve(int _t){
	int n, sum = 0;
	cin >> n;
	vector<int> cnt(n);
	for (int i = 0; i < n; i++){
		cin >> cnt[i];
		sum += cnt[i];
	}
	
	vector<pair<int, int> > plan;
	while (sum){
		for (int i = 0; i < n; i++){
			if (cnt[i] == 0) continue;
			cnt[i]--;
			// find max;
			int mx = 0;
			for (int p = 0; p < n; p++){
				if (cnt[mx] < cnt[p])
					mx = p;
			}

			if (cnt[mx] <= (sum - 1) / 2){
				//push out one and system is stable
				plan.pb(mp(i, -1));
				--sum;
				break;
			}
			else{
				//pushing out 1 makes system unstable
				//try pushing out two;
				cnt[mx]--; //remove one from max

				int mxx = 0;
				for (int p = 0; p < n; p++){
					if (cnt[mxx] < cnt[p])
						mxx = p;
				}

				if (cnt[mxx] <= (sum - 2) / 2){
					//success in making system stable
					plan.pb(mp(i, mx));
					sum -= 2;
					break;
				}
				else{
					//still unstable
					//restore system
					cnt[mx]++;
					cnt[i]++;
				}
			}
		}
	}
	cout << "Case #"<<_t<<": " ;
	for (int i = 0; i < plan.size(); i++){
		if (plan[i].second == -1)
			cout << (char)(65 + plan[i].first) << " ";
		else cout << (char)(65 + plan[i].first) << (char)(65 + plan[i].second) << " ";
	}
	cout << endl;
}
int main(){
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++){
		solve(i);
	}
	return 0;
}