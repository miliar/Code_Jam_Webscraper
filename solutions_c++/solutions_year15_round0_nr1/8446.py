#include <bits/stdc++.h>
using namespace std;

int main(){
	int t,smax,i,j;cin>>t;j=0;
	while(t--){
		j++;
		cin>>smax;char c[smax+1];int a[smax+1];
		int ans=0,raised=0;
		for(i=0;i<=smax;i++){
			cin>>c[i];a[i]=(int)c[i]-48;
		}
		//here onwards main loop starts.
		raised=a[0];
		for(i=1;i<=smax;i++){
			if(raised<i && a[i]){ans+=(i-raised);raised+=(i-raised);}
			raised+=a[i];
		}
		cout<<"Case #"<<j<<": "<<ans<<endl;
	}
}
