#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<list>
#include<queue>
#include<cmath>
#include<functional>
#include<algorithm>
#define INF (1<<29)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
using namespace std;



int t,a[4][4],b[4][4];

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	vector<int> ans;
	int t;
	cin>>t;
	rep(i,t){
		ans.clear();
		int x,y;
		cin>>x;
		rep(j,4)rep(k,4)cin>>a[j][k];
		cin>>y;
		rep(j,4)rep(k,4)cin>>b[j][k];
		rep(j,4){
			rep(k,4)if(a[x-1][j]==b[y-1][k])ans.push_back(a[x-1][j]);
		}
		cout<<"Case #"<<i+1<<": ";
		if(ans.size()==0)cout<<"Volunteer cheated!";
		else if(ans.size()==1)cout<<ans[0];
		else cout<<"Bad magician!";
		cout<<endl;
	}
	return 0;
}