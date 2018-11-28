#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
	int test;
	ll x,k,y;
	cin>>test;
	for(int te=1;te<=test;te++){
		cin>>x;
		int D[10]={0};
		bool sw=1,sw1;
		k=1;
		if(x==0)sw=0;
		while(sw){
			y=x*k;
			while(y>0){
				D[y%10]++;
				y/=10;
			}
			sw1=1;
			for(int i=0;i<10;i++)if(D[i]==0)sw1=0;
			if(sw1)break;
			k++;
		}
		cout<<"Case #"<<te<<": ";
		if(sw)cout<<x*k<<endl;
		else cout<<"INSOMNIA"<<endl;
	}
	return 0;
}
