#include<bits/stdc++.h>
 
using namespace std;
typedef long long ll;

int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	
	ll t,tc = 1;
	cin>>t;
	while(t--){
		ll n;
		cin>>n;
		if(n == 0)
		cout<<"Case #"<<tc<<": INSOMNIA"<<endl;
		else{
			ll i = 1;
			set<int> dig;
			while(dig.size() < 10)
			{
				ll j = i*n;
				while(j){
					dig.insert(j%10);
					j/=10;
				}
				i++;	
			}
			cout<<"Case #"<<tc<<": "<<(i-1)*n<<endl;
		}
		
		tc++;
	}
	return 0;
} 
