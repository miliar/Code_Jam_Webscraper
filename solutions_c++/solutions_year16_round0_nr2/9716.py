#include "bits/stdc++.h"
using namespace std;
string cad;
bool verifi(){
	bool sw=true;
	for (int i = 0; i < cad.length(); ++i)
	{
		if(cad[i]!='+')sw=false;
	}
	return sw;
}
void cambio(int n){
	for (int i = 0; i < n; ++i)
	{
		if(cad[i]=='+')cad[i]='-';
		else cad[i]='+';
	}
}
int main(){
	int t;
	cin>>t;
	for(int l=1;l<=t;l++){
		cin>>cad;
		int cont=0;
		while(!verifi()){
			for (int i = 0; i < cad.length(); ++i)
			{
				if(i!=cad.length()-1){
					if(cad[i]!=cad[i+1]){
						cambio(i+1);
						cont++;
						break;
					}
				}
				else {
					cambio(i+1);
					cont++;
				}
			}
		}
		cout<<"Case #"<<l<<": "<<cont<<endl;
	}
	return 0;
}