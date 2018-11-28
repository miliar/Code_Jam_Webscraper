#include <iostream>
#include <algorithm>
using namespace std;
int main(){
	int T;
	string cad, aux, solve;
	cin>>T;
	for (int c = 1; c <= T; ++c){
		cin>>cad;
		solve="";
		solve.push_back(cad[0]);
		for (int i = 1; i < cad.length(); ++i){
			if(cad[i]<solve[0])
				solve.push_back(cad[i]);
			else{
				aux="";
				aux.push_back(cad[i]);
				aux+=solve;
				solve=aux;
			}
		}
		cout<<"Case #"<<c<<": "<<solve<<endl;
	}


return 0;	
}