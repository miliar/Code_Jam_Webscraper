//https://code.google.com/codejam/contest/8234486/dashboard#s=p3
#include <iostream>
using namespace std;
#define M 1000000007
typedef long long ll;
ll dp[101][13][32]; //2*, [3;3]*, [122;122]*, 2-spiral, 3-spiral
#define nrot 13
#define ntype 2

#define ACC(X,Y) X=(((X)+(Y))%M)
#define DP(i,j,j0,r)	ACC(dp[i][j][0],r*dp[i-h][j0][1])

int calc(int r, int c){
	int i,j,h;
	for (i=0; i<=r; i++) for (j=0; j<nrot; j++) dp[i][j][0]=dp[i][j][1]=0;

	dp[1][1][0]+=1; 
	dp[2][1][1]+=1;
	if (c%3==0) dp[2][3][0]+=1; 
	if (c%6==0) dp[2][6][0]+=1;
	if (c%4==0) dp[3][4][0]+=1;

	for (i=3; i<=r; i++){
		for (j=0; j<nrot; j++){
			h=1;
			ACC(dp[i][j][0],dp[i-h][j][1]);
			h=2;
			ACC(dp[i][j][1],dp[i-h][j][0]);
		}
		h=2;
		if (i>h && c%3==0){
			DP(i,3,1,1); 
			DP(i,3,3,3);
			DP(i,6,6,3);
			DP(i,12,4,4);
			DP(i,12,12,3);
		}
		if (i>h && c%6==0){
			DP(i,6,1,1);
			DP(i,6,3,3);
			DP(i,6,6,6);
			DP(i,12,4,4);
			DP(i,12,12,6);
		}
		h=3;
		if (i>h && c%4==0){
			DP(i,4,1,1);
			DP(i,12,3,3);
			DP(i,12,6,6);
			DP(i,4,4,4);
			DP(i,12,12,4);
		}
	}
	ll res=0;
	for (i=0; i<2; i++) for (j=0; j<nrot; j++) ACC(res,dp[r][j][i]);
	return res;
}

int main(){
	int u,i,t,r,c,res;
	cin>>t; for (u=0; u<t; u++){
		cin>>r>>c;
		if (r==1) res=1;
		else res=calc(r,c);
		cout<<"Case #"<<(u+1)<<": "<<res<<endl;
	}
	return 0;
}
