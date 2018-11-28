#include<bits/stdc++.h>

using namespace std;

int pan[1005], maxN;

int main(){

	int T, n;
	freopen("Blarge.in","r",stdin);
	freopen("Blarge.out","w",stdout);
	
	cin >> T;
	
	for(int tc = 1; tc <= T; tc ++){
		
		int ans = 100000000, sol = 0;
		priority_queue<int> q;
		
		cin >> n;
		maxN = 0;
		
		for(int i = 0; i < n; i ++){
			cin >> pan[i];
			maxN = max(maxN, pan[i]);
		}
			
		for(int i = 1; i <= maxN; i ++){
			sol = 0;
			for(int j = 0; j < n; j ++){
				if(pan[j] > i){
					sol += ceil(pan[j]*(1.0) / (i * 1.0));
					sol --;
				}
			}
			ans = min(ans, sol + i);
		}
		printf("Case #%d: %d\n",tc, ans);
	}
	
	return 0;
}
