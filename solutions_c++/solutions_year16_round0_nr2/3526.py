#include <bits/stdc++.h>
using namespace std;

string s;
int dp[105][505];

int findMin(int i, int flips){
	if(i==-1)
		return flips;
	if(dp[i][flips] != -1)
		return dp[i][flips];
	int ans = 1e9;
	int j = flips;
	bool canEvenFlips = s[i]=='+';
	if(canEvenFlips && j%2 != 0) j++;
	else if(!canEvenFlips && j%2 == 0) j++;
	for(;j<=500;j+=2){
		ans = min(ans,findMin(i-1,j));
	}
	return dp[i][flips] = ans;
}

int main(){
	// freopen("inputp2.txt","r",stdin);
	// freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	for(int c=1;c<=t;c++){
		memset(dp,-1,sizeof(dp));
		cin>>s;
		cout<<"Case #"<<c<<": "<<findMin(s.length()-1,0)<<endl;
	}
	return 0;
}