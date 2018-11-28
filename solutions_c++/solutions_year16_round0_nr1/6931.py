#include<bits/stdc++.h>
using namespace std;
#define ll long long
int hash(int f[], ll a){
	while(a){
		f[a%10]=1;
		a=a/10;
	}
	
	//~ for(int i=0;i<=9;i++)
		//~ cout<<f[i];
	//~ cout<<'\n';
	
	for(int i=0;i<=9;i++)
		if(!f[i])
			return 0;
	return 1;
}
int main(){
	cout.sync_with_stdio(0);
	cin.tie(0);
	int t,te=1;
	cin>>t;
	while(t--){
		ll a;
		cin>>a;
		
		int f[10]={0},flag=0;
		ll i=1;
		for(int i1=0;i1<=100000;i1++){
			ll b=a*i;
			if(hash(f,b)){
				cout<<"Case #"<<te++<<": "<<b<<'\n';
				flag=1;
				break;
			}
			i++;
		}
		if(!flag) 
			cout<<"Case #"<<te++<<": INSOMNIA\n";
	}
}
