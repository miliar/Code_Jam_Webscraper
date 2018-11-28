#include<bits/stdc++.h>

using namespace std;

int n,dp[1005][1005];
int pan[1005];

int cell(int x, int y){
	return (int) ceil( x*1.00/y );
}

int play(int pos, int elapsed){
	if(pos==n) return 0;
	int &ret=dp[pos][elapsed];	
	if(ret!=-1) return ret;
	
	ret=max(0,pan[pos]-elapsed)+play(pos+1,max(elapsed,pan[pos]));
	for(int y=2;y<=pan[pos];y++){
		ret=min(ret,y-1+max(0,cell(pan[pos],y)-elapsed)+play(pos+1,max(elapsed,cell(pan[pos],y) )) );
	}
	return ret;
}

int main(){
	int t;
	freopen("out.txt","w",stdout);
	
	scanf("%d",&t);
	
	for(int tc=1;tc<=t;tc++){
		
		memset(dp,-1,sizeof dp);
		scanf("%d",&n);
		
		for(int x=0;x<n;x++) scanf("%d",&pan[x]);
		
		printf("Case #%d: %d\n",tc ,play(0,0));
		
		
	}

}
