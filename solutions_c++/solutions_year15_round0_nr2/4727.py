#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <queue>

using namespace std;
int T,D;
int P[1005];
priority_queue<int> pq;
int main(){
	
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> T;
	
	for(int t = 1; t <= T; ++t){
		
		cin >> D;
		for(int i = 0; i < D; ++i){
			cin >> P[i];		
		}
		int ans = 99999;
		for(int i = 1;  i <= 10; ++i){
			int q = 0;
			for(int j = 0; j < D; ++j)
				if(P[j] > i)
					q += (P[j]-1)/i;
			ans = min(ans, q + i);
		}
			
			
		cout << "Case #" << t << ": " << ans << endl;
	}
	
	
	
}
