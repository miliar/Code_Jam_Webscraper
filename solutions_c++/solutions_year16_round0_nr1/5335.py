#include<bits/stdc++.h>
#include<cstdlib>
using namespace std;
#define ll long long

int main(){
	int t,temp=1;
	cin>>t;
	while(temp!=t+1){
		ll n;
		cin>>n;
		cout<<"Case #"<<temp<<": ";
		temp++;
		int a[10];
		memset(a,0,sizeof(a));
		if(n==0){
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		ll count = 1;
		bool flag = false;
		while(true){
			ll current = n*count;
			count++;
			stringstream ss;
			ss << current;
			string str = ss.str();
			
			for(ll i=0;i<str.length();i++){
				//cout<<str[i];
				if(!a[str[i]-'0'])
					a[str[i]-'0'] = 1;
				
			}
			//cout<<endl;
			ll check = 0;
			for(ll i=0;i<10;i++){
				if(a[i])
					check++;
			}
			if(check==10){
				cout<<current<<endl;
				break;
			}
		}
	
	}
	return 0;
}
