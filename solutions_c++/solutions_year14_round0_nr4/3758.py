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
	double a[1000],b[1000];
	cin>>t;
	rep(i,t){
		int n;
		cin>>n;
		rep(i,n)cin>>a[i];
		rep(i,n)cin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		int j,ansx=n,ansy=0;
		j=n-1;
		for(int i=n-1;i>=0;i--){
			while(j>=0&&a[i]<b[j])j--;
			if(j==-1){
				ansx=n-i-1;
				break;
			}
			j--;
		}
		j=0;
		rep(i,n){
			while(j<n&&a[i]>b[j])j++;
			if(j==n){
				ansy=n-i;
				break;
			}
			j++;
		}
		cout<<"Case #"<<i+1<<": "<<ansx<<' '<<ansy<<endl;
	}
	return 0;
}