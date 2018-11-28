#include <bits/stdc++.h>

using namespace std;

int main(){
	int t;
	int n;
	int aux;
	int aux2;
	int aux3;
	vector<bool> bizu;
	int cont=1;
	cin>>t;
	while(t--){
		cout<<"Case #"<<cont<<": ";
		cont++;
		bizu=vector<bool>(10,false);
		cin>>n;
		if(n==0){
			cout<<"INSOMNIA\n";
			continue;
		}
		aux=0;
		aux3=0;
		while(aux3!=10){
			aux+=n;
			aux2=aux;
			while(aux2!=0){
				if(!bizu[aux2%10]){
					bizu[aux2%10]=true;
					aux3++;
				}
				aux2/=10;
			}
		}
		cout<<aux<<"\n";
	}
	return 0;
}