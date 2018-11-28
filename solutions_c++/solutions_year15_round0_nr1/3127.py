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


int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin>>t;
	rep(i,t){
		int sm,n=0,ans=0;
		string s;
		cin>>sm>>s;

		rep(j,sm+1){
			int d=s[j]-'0';
			ans+=max(0,j-n);
			n+=d+max(0,j-n);
		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}