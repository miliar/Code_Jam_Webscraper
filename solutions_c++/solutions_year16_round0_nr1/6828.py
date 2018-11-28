#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
set<int> s;
void add(ll d){
	while(d){
		s.insert(d%10);
		d/=10;
	}
} 
int main(){
	int t;
	ll d;
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>d;
		if(d==0){
			printf("Case #%d: INSOMNIA\n",i);
		}
		else{
			s.clear();
			ll k=0;
			while(s.size()<10){
				k+=d;
				add(k);
			}
			printf("Case #%d: %lld\n",i,k);
		}
	}
}