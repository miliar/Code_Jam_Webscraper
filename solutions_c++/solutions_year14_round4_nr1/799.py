#include<iostream>
#include<algorithm>
#include<cstdio>
using namespace std;
int a[100011];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int T;cin>>T; int tt=0;
	
	while(T--) {
		int n,k;
		cin>>n>>k;
		for(int i=1;i<=n;i++){
			cin>>a[i];
		}
		sort(a+1,a+1+n);
		int l=1,r=n; int tot= 0 ;
		while(l<=r){
			if(a[l]+a[r]<=k) {
				l++; r--; tot++;
			}else {
				r--; tot++;
			}
		}
		cout<<"Case #"<<++tt<<": "<<tot<<"\n";
	}
	return 0;
}

