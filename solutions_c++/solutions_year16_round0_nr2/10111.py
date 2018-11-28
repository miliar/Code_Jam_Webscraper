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
	int t ; 
	cin>>t ; 
	string S; 
	int change ; 
	for(int i=1;i<=t;i++){
		cin>>S; 
		change = 0 ; 
		S = S+"+";
		char pre = S[0];
		for(int j=0;j<S.length();j++){
			if(S[j]!=pre){ 
				pre = S[j] ; 
				change++;
			}
		}
		cout<<"Case #"<<i<<": "<<change<<endl ;
	}
}