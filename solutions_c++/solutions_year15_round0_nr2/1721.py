#include<iostream>
#include<cstdio>
#include<sstream>
#include<fstream>
#include<cctype>
#include<cstdlib>
#include<cmath>
#include<ctime>
#include<cstring>
#include<string>
#include<complex>
#include<bitset>
#include<map>
#include<set>
#include<vector>
#include<algorithm>
#include<queue>
#include<deque>
#include<stack>
#include<iomanip>
#include<utility>

#define pb push_back
#define pp pop_back
#define xx first
#define yy second
#define mp make_pair

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

const int maxn=1000+10;
int t,n,a[maxn],dp[maxn][maxn];
int get(int x,int y){
	int &ret=dp[x][y];
	if(ret!=-1)return ret;
	if(y<=x)return ret=0;
	ret=1e9;
	for(int i=1;i<y;i++)ret=min(ret,get(x,i)+get(x,y-i)+1);
	return ret;
}
int solve(int x){
	int ret=x;
	for(int i=1;i<=n;i++)if(a[i]>x)ret+=dp[x][a[i]];	
	return ret;
}
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	memset(dp,-1,sizeof(dp));
	for(int i=1;i<=1000;i++)for(int j=1;j<=1000;j++)get(i,j);
	cin>>t;
	for(int l=1;l<=t;l++){
		cin>>n;
		int mx=0,ans=1e9;
		for(int i=1;i<=n;i++){
			cin>>a[i];
			mx=max(mx,a[i]);
		}
		for(int j=1;j<=mx;j++)ans=min(ans,solve(j));
		cout<<"Case #"<<l<<": "<<ans<<endl;
	}
	return 0;
}
