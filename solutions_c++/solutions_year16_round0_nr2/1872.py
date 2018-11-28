#include <bits/stdc++.h>

using namespace std;

int main(){
	int t;
	string p;
	int aux;
	int cont=1;
	cin>>t;
	while(t--){
		cout<<"Case #"<<cont<<": ";
		cont++;
		aux=0;
		cin>>p;
		for(int i=1;i<p.size();i++)
			if(p[i]!=p[i-1])
				aux++;
		cout<<aux+(p[p.size()-1]=='-'?1:0)<<"\n";
	}
	return 0;
}