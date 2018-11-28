#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;

int dp[1 << 21][40];
bool calcdp[1 << 21];
int rest[1 << 21][40];
int keys[21][40];
int open[21];

bool mless(int mask, int newmask, int cnt){
	if (calcdp[newmask] == 0)
		return true;
	for (int i = 0; i < cnt; i++)
		if (dp[mask][i] < dp[newmask][i])
			return true;
		else if (dp[mask][i] > dp[newmask][i])
			return false;
	return false;
}

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int T;
	cin>>T;

	for (int t = 0; t < T; t++){
		int k, n;
		cin>>k>>n;

		for (int i = 0; i < (1 << n); i++){
			calcdp[i] = 0;
			for (int j = 0; j < 40; j++){
				rest[i][j] = 0;
				dp[i][j] = 0;
			}
		}

		for (int i = 0; i < n; i++)
			for (int j = 0; j < 40; j++)
				keys[i][j] = 0;
		
		calcdp[0] = 1;
		for (int i = 0; i < k; i++){
			int temp;
			cin>>temp;
			rest[0][temp]++;
		}

		for (int i = 0; i < n; i++){
			cin>>open[i];
			int ki;
			cin>>ki;
			for (int j = 0; j < ki; j++){
				int temp;
				cin>>temp;
				keys[i][temp]++;
			}
		}

		for (int mask = 0; mask < (1 << n); mask++){
			if (calcdp[mask] == 0)
				continue;

			int cnt = 1;
			for (int i = 0; i < n; i++)
				if (mask & (1 << i))
					cnt++;

			for (int i = 0; i < n; i++){
				if (mask & (1 << i)){
					continue;
				}
				if (rest[mask][open[i]] > 0){
					dp[mask][cnt - 1] = i + 1;
					int newmask = mask | (1 << i);
					if (mless(mask, newmask, cnt)){
						calcdp[newmask] = 1;
						for (int j = 0; j < cnt; j++)
							dp[newmask][j] = dp[mask][j];
						for (int j = 0; j < 40; j++)
							rest[newmask][j] = rest[mask][j] + keys[i][j];
						rest[newmask][open[i]]--;
					}
				}
			}
		}

		cout<<"Case #"<<t + 1<<":";
		
		if (calcdp[(1 << n) - 1]){
			for (int i = 0; i < n; i++)
				cout<<" "<<dp[(1 << n) - 1][i];
		}
		else
			cout<<" IMPOSSIBLE";

		cout<<endl;;
	}
}