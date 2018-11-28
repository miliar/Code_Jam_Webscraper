//#include <iostream>
//#include <cstring>
#include <bits/stdc++.h>
using namespace std;

bool V[11];
typedef long long ll;
void Solve(ll x){
	while(x>0){
		ll mod=x%10;
		V[mod]=true;
		x=x/10;
	}
	return;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("Output2.out","w",stdout);
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	ll tc,x,c,i,sum,cp=0;
	cin>>tc;
	while(tc--){
		memset(V,false,sizeof(V));
		cin>>x;
		cout<<"Case #"<<++cp<<": ";
		sum=x;
		c=0;
		bool ans=false;
		while(c<=100000){
			c++;
			Solve(sum);
			for(i=0;i<10;i++){
				//cout<<i<<":"<<V[i]<<endl;
				if(V[i]==false) break;
			}
			if(i==10){
				ans=true; break;
			}
			sum+=x;
		}
		if(ans) cout<<sum<<endl;
		else cout<<"INSOMNIA"<<endl;
	}
}
