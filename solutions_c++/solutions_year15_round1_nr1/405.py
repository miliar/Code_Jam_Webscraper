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


int a[1000];

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin>>t;
	rep(testcase,t){
		int ans1,ans2;
		int n;
		ans1=ans2=0;
		cin>>n;
		rep(i,n)cin>>a[i];

		for(int i=1;i<n;i++){
			ans1+=max(0,a[i-1]-a[i]);
		}
		int maxdec=0;
		for(int i=1;i<n;i++){
			maxdec=max(maxdec,a[i-1]-a[i]);
		}
		for(int i=1;i<n;i++){
			ans2+=min(a[i-1],maxdec);
		}

		cout<<"Case #"<<testcase+1<<": "<<ans1<<' '<<ans2<<endl;
	}
	return 0;
}