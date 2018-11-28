#include <iostream>

using namespace std;


int rev(int x){
	int ret = 0;
	while(x){
		ret = ret*10 + x%10;
		x/=10;
	}
	return ret;
}

int n;

bool visited[10000005];
int dp[1000005];
int find(int curr=1){
	if(curr > 1e6)
		return 1e9;
	if(curr == n)
		return 1;
	if(dp[curr]!=-1)
		return dp[curr];
	if(visited[curr])
		return 1e9;
	visited[curr] = true;
	int r = rev(curr);
	if(r>curr)
		return dp[curr]=min(find(r),find(curr+1)) +1;
	else return dp[curr]=find(curr+1)+1;
}

int main(){
	ios::sync_with_stdio(false);
	freopen("gcj1.txt","r",stdin);
	freopen("output4.txt","w",stdout);

	int i,t,c=1;
	cin>>t;
	while(t--){
		cin>>n;
		cout<<"Case #"<<c++<<": ";
		memset(dp,-1,sizeof(dp));
		memset(visited,0,sizeof(visited));
		cout<<find()<<endl;
	}
}