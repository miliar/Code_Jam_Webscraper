#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ll;

int main(){
	int n;
	int tc; 
	cin>>tc;
	for(int tt=1;tt<=tc;tt++){
		cin>>n;	
		ll currfinal = n;
		set<int> hash;
		for(ll i=1;i<10000000000;i++){
			ll curr = n*i;
			//cout<<curr<<endl;
			currfinal = curr;
			if(curr==0)
				break;
			else{
				while(curr!=0){
					hash.insert(curr%10);
					curr/=10;
				}
			}
			if(hash.size()==10){
				break;
			}
		}
		printf("Case #%d: ",tt );
		if(currfinal==0)
			cout<<"INSOMNIA"<<endl;
		else
			cout<<currfinal<<endl;

	}
}