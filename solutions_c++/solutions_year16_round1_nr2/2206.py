#include <bits/stdc++.h>
using namespace std;
int main(){
	int t, n, aux;
	map<int, int>mapa;
	map<int, int>::iterator it;
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>n;
		for(int j=0;j<(2*n*n -n);j++){
			cin>>aux;
			//cout<<aux<<endl;
			mapa[aux]++;
		}
		cout<<"Case #"<<i<<":";
		for(it=mapa.begin();it!=mapa.end();it++){
			if((it->second) %2==1){
				cout<<" "<<it->first;
			}
		}
		mapa.clear();
		cout<<endl;
	}
	return 0;
}
