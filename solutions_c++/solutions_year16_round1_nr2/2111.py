
#include<bits/stdc++.h>
#define all(x) x.begin(), x.end()
#define pb(x) push_back(x)
#define cout2(x, y) cout << x << " " << y << endl
#define N 55

using namespace std;

int frec[2505];

int main(){

	int tc = 0, caso = 1;
	scanf("%d", &tc);
	
	while(tc--){
		
		int n, x;
		scanf("%d", &n);
		
		memset(frec, 0, sizeof frec);
		
		for(int i = 0; i < 2 * n - 1; i++){
			
			for(int j = 0; j < n; j++){
				scanf("%d", &x);
				frec[x]++;
			}
			
			
		}
		
		vector<int>ans;
		for(int i = 1; i <= 2500; i++)if(frec[i]&1)ans.pb(i);
		
		printf("Case #%d:", caso++);
		for(int j = 0; j < ans.size(); j++)printf(" %d", ans[j]);
		puts("");
		
	}


}


