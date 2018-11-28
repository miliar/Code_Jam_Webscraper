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
		set <int> s; 
		
		long long ans, tans; 
		for(int i=1; i<=101;i++){
			ans =n*i ; 
			tans =ans ;
			while(ans){ 
				s.insert(ans%10); 
				ans = ans/10; 
			}

			if(s.size()>=10){
				break ; 
			}  
		}
		if(s.size()>=10){ 
			cout<<tans<<endl ; 
		}
		else cout<<"INSOMNIA"<<endl; 
	}
	
}