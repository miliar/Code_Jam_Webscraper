#include <iostream>
using namespace std;
int main(){
	int T;
	cin>>T;
	for (int c = 1; c <= T; ++c){
		string cad, cad1;
		cin>>cad;
		cout<<"Case #"<<c<<": ";
		cad1.push_back(cad[0]);
		for (int i = 1; i < cad.length(); ++i){
			if(cad1[cad1.length()-1] != cad[i])
				cad1.push_back(cad[i]);
		}
		if(cad1.length()%2==0){
			if(cad1[0]=='+')
				cout<<cad1.length();
			else
				cout<<cad1.length()-1;
		}
		else{
			if(cad1[0]=='+')
				cout<<cad1.length()-1;
			else
				cout<<cad1.length();
		}	
		cout<<endl;
		
	}
	return 0;
}