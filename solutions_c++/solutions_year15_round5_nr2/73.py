#include<iostream>
#include<algorithm>
using namespace std;


int T, n, k, sum[10000], cdiff[1000], maxdiff[1000], mindiff[1000];





int main() {
	cin.sync_with_stdio(false);
	
	cin >> T;
	
	for(int TCASE=1;TCASE <= T;TCASE++) {
		cin >> n >> k;
		
		for(int i=0;i<n-k+1;i++)
			cin >> sum[i];
			
		
		fill(cdiff, cdiff + n, 0);
		fill(maxdiff, maxdiff + n, 0);
		fill(mindiff, mindiff + n, 0);
		
		
		
		for(int i=0 ;  i+1 < n-k+1  ; i++) {
			cdiff[i%k] += sum[i+1] - sum[i];
			
			maxdiff[i%k] = max(maxdiff[i%k], cdiff[i%k]);
			mindiff[i%k] = max(mindiff[i%k], -cdiff[i%k]);
		}
		
		
		int result = 0;
		
		for(int i=0;i<k;i++)
			result = max(result,  mindiff[i] + maxdiff[i]);
		
		
		int smod = 0, wiggle = 0;
		
		for(int i=0;i<k;i++) {
			smod += mindiff[i];
			
			wiggle += result - (maxdiff[i] + mindiff[i]);
		}
		
		
		smod %= k;
		
		int require = (sum[0] % k + k) % k;
		
		if( (require + k - smod) % k > wiggle)
			result++;
		
		
		cout << "Case #" << TCASE << ": " << result << '\n';
		
	}
	
	return 0;
}




































