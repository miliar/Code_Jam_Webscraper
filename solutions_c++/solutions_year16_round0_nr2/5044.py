#include <bits/stdc++.h>

using namespace std;

int dp[1024][12];
char s[12];

int calc(int mask, int p){
	if(dp[mask][p] != -1) return dp[mask][p];
	if(p == 1) return dp[mask][p] = (mask == 0);
	if(mask == (1 << p) - 1) return dp[mask][p] = 0;
	if(mask & (1 << (p-1))) return dp[mask][p] = calc(mask - (1 << (p-1)), p - 1);
	int res = 1000000;
	if(mask & 1){
		for(int i = 0; i < p; i++){
			if((mask & (1 << i))) continue;
			int l = i + 1;
			int m = 0;
			for(int j = 0; j < l; j++){
				m = m * 2 + !((mask >> (l - j - 1)) & 1);
			}
			for(int j = l; j < p; j++){
				m = m * 2 + ((mask >> j) & 1);
			}
			res = min(res,calc(m,p));
		}
	}
	else{
		int m = 0;
		for(int i = 0; i < p; i++){
			m = m * 2 + !((mask >> (p - i - 1)) & 1);
		}
		while(p > 0 && (m & (1 << (p - 1)))){
			m -= (1 << (p - 1));
			p--;
		}
		res = min(res,calc(m,p));
	}
	return dp[mask][p] = 1 + res;
}

void init(){
	int T;
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
		memset(dp,-1,sizeof(dp));
		scanf("%s",s);
		int l = strlen(s);
		int mask = 0;
		for(int i = 0; i < l; i++){
			mask = mask * 2 + (s[l-i-1] == '+');
		}
		int res = calc(mask,l);
		printf("Case #%d: %d\n",t,res);
	}
}

void fread(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

int main(){
	fread();
	init();
	return 0;
}