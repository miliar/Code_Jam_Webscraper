#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
using namespace std;
int a[100001],b[100001];

int n;
bool check() {
	int Find=0;
	for(int i=1;i<=n-1;i++){
		if(Find==0){
			if(a[i+1]<a[i]) Find=1;
		}else {
			if(a[i+1]>a[i]) return 1;
		}
	}
	return 0;
}
int l[10001],r[10001];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T; cin>>T; int tt=0;
	while(T--){
		cin>>n;
		memset(l,0,sizeof l);
		memset(r,0,sizeof r);
		for(int i=1;i<=n;i++)cin>>a[i];
		for(int i=1;i<=n;i++){
			for(int j=1;j<=i;j++) if(a[j]>a[i])l[i]++;
			for(int j=i;j<=n;j++) if(a[i]<a[j])r[i]++;
		}
		int Max=0; for(int i=1;i<=n;i++) Max+=min(l[i],r[i]);
		cout<<"Case #"<<++tt<<": "<<Max<<endl;
	}
	return 0;
}