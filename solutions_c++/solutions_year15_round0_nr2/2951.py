#include<bits/stdc++.h>
using namespace std;
int main(){
	int t,r;
//	freopen("1.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	cin>>t;
	for(int r=1;r<=t;r++){
		int n,temp;
		cin>>n;
		int mx=-1;
		int a[n];
		for(int i=0;i<n;i++){
			cin>>a[i];
			mx=max(mx,a[i]);
		}
		int ans=mx;
		//cout<<mx<<"%$\n";
		for(int i=1;i<=mx;i++){
			int temp=0,mx2=0;
			for(int j=0;j<n;j++){
				if(a[j]>i){	
					temp+=(a[j]/i)-1;
					if(a[j]%i!=0)
					temp++;
					mx2=max(mx2,i);
				} else
				mx2=max(a[j],mx2);
			}
			temp+=mx2;
			if(ans>temp)
			ans=temp;
		}
		//cout<<temp<<endl;
		cout<<"Case #"<<r<<": "<<ans<<"\n";
	}
	return 0;
}

