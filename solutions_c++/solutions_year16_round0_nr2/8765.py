#include <iostream>
#include <string>
using namespace std;

int sol(string cad){
	int res=0 , aux =cad.size();
	for(int i=aux-1 ; i>=0;i--){
		if(cad[i]=='-'){
			res++;
			while(i>=0 && cad[i]!='+') i--;
			if(i>=0 && cad[i]=='+') res++;
		}
	}
	return res;
}

int main() {
	int T; cin>>T;
	for(int i=1;i<=T;i++){
		string cad;cin>>cad;
		cout<<"Case #"<<i<<": "<<sol(cad)<<endl;
	}
	return 0;
}