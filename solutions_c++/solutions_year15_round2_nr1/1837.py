
#include<bits/stdc++.h>
#define all(x) x.begin(), x.end()
#define pb(x) push_back(x)
#define N 1000002
#define cout2(x, y) cout << x << " " << y << endl
using namespace std;

int trans(int n){
	
	int ans = 0;
	while(n > 0)ans = ans * 10 + n%10, n/= 10;
	return ans;	
}

int Q[N + 5], D[N + 5], next[2][N + 5];

void solve(){
	
	memset(D, -1, sizeof D);
	D[1] = 1;
	
	int head = 0, tail = 0;
	Q[tail++] = 1;
	
	while(head < tail){
		
		int u = Q[head++];
		int v = next[0][u];
		
		if(D[v] == -1){
			
			D[v] = D[u] + 1;
			Q[tail++] = v;
		}
		
		v = next[1][u];
		if(D[v] == -1){
			
			D[v] = D[u] + 1;
			Q[tail++] = v;
		}	
	}
	
}

int main(){

	for(int i = 1; i < N; i++){
			
		next[0][i] = i + 1;
		next[1][i] = trans(i);
	}
	
	solve();
	
	int tc = 0, caso = 1;
	scanf("%d", &tc);
	
	while(tc--){
		
		int n;
		scanf("%d", &n);
		
		printf("Case #%d: %d\n", caso++, D[n]);
	}


}

