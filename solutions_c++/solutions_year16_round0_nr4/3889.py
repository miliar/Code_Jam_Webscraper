#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	int T,K,C,S;
	cin>>T;
	for(int l=1;l<=T;l++){
		cin>>K>>C>>S;
		if(ceil(K/C)>S) {
			cout<<"Case #"<<l<<": "<<"IMPOSSIBLE\n";
		}
		else{
			cout<<"Case #"<<l<<":";
			for(int i=0;i<K;){
				long long Temp=0;
				for(int j=0;j<C&&i<K;j++){
					Temp=Temp*K+i;
					i++;
				}
				cout<<" "<<Temp+1;
			}
			cout<<"\n";
		}
	}
}
