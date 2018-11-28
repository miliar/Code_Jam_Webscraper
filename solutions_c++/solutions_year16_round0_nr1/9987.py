#include <bits/stdc++.h>
using namespace std  ;

#define pb push_back  
#define mp make_pair
typedef long long ll ; 
typedef vector <ll> vll;
typedef vector <int> vint ;
ll mod = int(1e9+7) ;
const ll maxx = int(100005) ; 


int main(){
	long long t,n ; 
	cin>>t ; 

	for(int j=1;j<=t;j++){ 

		
		cin>>n ; 
		cout<<"Case #"<<j<<": ";
		set <int> S; 
		
		long long ans = n, k = 0 ,temp ; 
		for(int i=1; i<=101;i++){
			ans =n*i ; 
			temp = ans ; 
			while(ans){ 
				S.insert(ans%10); 
				ans = ans/10; 
			}

			if(S.size()>=10){
				k = 1 ; break ; 
			}  
		}
		if(k==1){ 
			cout<<temp<<endl ; 
		}
		else cout<<"INSOMNIA"<<endl; 
	}
	
}