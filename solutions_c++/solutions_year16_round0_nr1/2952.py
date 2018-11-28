#include<bits/stdc++.h>
#define ll long long

using namespace std;

bool ten[10];

int main(){
	
	ll t,n,n1,k;
	cin>>t;
	for(int j=1;j<=t;j++){
		cin>>n;
		n1=n;
		if(n==0)cout<<"Case #"<<j<<": "<<"INSOMNIA"<<"\n";
		else {
			for(int i=0;i<10;i++)ten[i]=false;
			while(true){
				k=n;
				while(k>0){
					ten[k%10]=1;
					k/=10;
				}
				bool f=true;
				for(int i=0;i<10;i++){
					if(!ten[i]){
						f=false;break;
					}
				}
				if(f)break;
				n+=n1;
			}
			cout<<"Case #"<<j<<": "<<n<<"\n";
		}
	}
	return 0;
}
