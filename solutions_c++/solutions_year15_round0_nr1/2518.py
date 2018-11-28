#include <bits/stdc++.h>
using namespace std;
int levels[1010];

int main(){
	int T; cin >> T;
	for(int t = 0; t < T; t++){
		memset(levels,0,sizeof levels);
		int k; cin >> k;
		for (int i = 0; i < k+1; i++){
			char c; cin >> c;
			levels[i]=(int)(c-'0');
		}
		int ans = 0;
		int curr_sum = 0;
		for (int i = 0; i < k+1; i++){
			if (curr_sum < i) {
				ans+=(i-curr_sum);
				curr_sum = i; 
			}
			curr_sum+=levels[i];
		}
		cout << "Case #" << t+1 << ": " << ans << endl;
	}
	return 0;
}
