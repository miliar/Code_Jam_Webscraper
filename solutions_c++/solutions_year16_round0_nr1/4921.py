#include<iostream>
#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
	ll t,n,digit,temp,ans,c=0;
	cin>>t;
	while(t--){c++;
		cin>>n;
		//n=c;
		if(n==0){
			cout<<"Case #"<<c<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		ll a[15]={0},flag=0;
		for(ll i=1;;i++){
			temp=i*n;
			ans=temp;
			 //temp=n;
			while(temp>0){
				digit=temp%10;
				temp/=10;
				a[digit]++;
			}
			for(ll j=0;j<10;j++){
				if(a[j]==0){
					flag=1;
					break;
				}
			}
			if(!flag)break;
			flag=0;
		}
	
		cout<<"Case #"<<c<<": "<<ans<<endl;
	}
	return 0;
}
