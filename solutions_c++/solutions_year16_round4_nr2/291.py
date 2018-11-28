#include <bits/stdc++.h> 

using namespace std;

#define ll long long
#define type double

int n,k;

type p[210];

type pp[210];

int cnt_bit(int x){
	int res = 0;
	while(x){
		if(x&1){
			res++;
		}
		x>>=1;
	}
	return res;
}

type dp[210][210];

type solve(){
	for(int i=0;i<=k;i++){
		for(int j=0;j<=i;j++){
			dp[i][j] = 0;
		}
	}
	
	dp[0][0] = 1;
	
	for(int i=1;i<=k;i++){
		dp[i][0] = dp[i-1][0] * (1.0-pp[i]);
		for(int j=1;j<=i;j++){
			dp[i][j] += dp[i-1][j] * (1.0-pp[i]);
			dp[i][j] += dp[i-1][j-1] * pp[i];
		}
	}
	return dp[k][k>>1];
}

int main(){
	freopen("B-large.in","r",stdin);
   	freopen("B-large.out","w",stdout);
	int t;
	cin>>t;
	
	int cas = 0;
	while(t--){
		
		cas++;
		cin>>n>>k;
		
		for(int i=1;i<=n;i++){
			cin>>p[i];
		}
		
		int End = (1<<n);
		type ans = 0;
		
		sort(p+1,p+n+1);
		
		for(int i=0;i<=k;i++){
			int large = k-i;
			int pos = 1;
			for(int j=0;j<i;j++){
				pp[pos++] = p[j+1];
			}
			for(int j=0;j<large;j++){
				pp[pos++] = p[n-j];
			}
			type tmp = solve();
			ans = max(ans,tmp);
		}
		
		/*for(int i=1;i<End;i++){
			if(cnt_bit(i)!=k){
				continue;
			}
			
			int pos = 1;
			for(int j=0;j<n;j++){
				if(i&(1<<j)){
					pp[pos++] = p[j+1];
		//			cout<<"!"<<p[j+1]<<endl;
				}
			}
			
			type tmp = solve();
			ans = max(ans,tmp);
		}*/
		
		printf("Case #%d: %.6f\n",cas,ans);
	}
	
	return 0;
}

/*
int min3(int a,int b,int c){
	return min(a,min(b,c));
}

int max3(int a,int b,int c){
	return max(a,max(b,c));
}

int main(){
	int t;
	cin>>t;
	
	while(t--){
		int n,r,p,s;
		cin>>n>>r>>p>>s;
		
		int MIN = min3(r,p,s);
		int MAX = max3(r,p,s);
		
		if(MIN+1<MAX){
			
		}
		
	}
	return 0;
}

*/
