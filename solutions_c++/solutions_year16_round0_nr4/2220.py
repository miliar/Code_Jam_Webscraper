#include <stdio.h>
#include <iostream>
using namespace std;

const int MAXN = 200;

int solve(long long K, long long C, long long S, long long ans[MAXN])
{
	// cout << K << " " << C << " " << S << " " << endl;
	if(C==1) {
		for(int i = 0;i < K; i++) ans[i] = i+1;
		return K;
	}

	long long B = 1;
	for(int i = 0;i<C-1;i++) B = B * K;

	int cnt = 0;
	for(long long i=0;i<K;i+=2){
		long long t = i*B+i+1;
		if(i+1>=K) t--;
		ans[cnt++] = t+1; 
	}
	// printf("cnt %d\n",cnt);
	return cnt;
}

int main()
{
	long long T,K,C,S;
	long long ans[MAXN];
	cin >> T;
	for(int i = 1; i<=T;i++){
		cin >> K >> C >> S;	
		printf("Case #%d: ",i);
		long long n = solve(K,C,S,ans);
		if(n>S) printf("IMPOSSIBLE\n");
		else{
			for(int j = 0;j<n;j++){
				if(j==n-1) cout << ans[j] << endl;
				else cout << ans[j] << " ";
			}
		}
	}
	return 0;
}
