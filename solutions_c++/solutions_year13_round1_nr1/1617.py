#include <iostream>
#include <cstring>
#include <cmath>
#include <sstream>
using namespace std;


int main(){
	int l;
	cin>>l;
	int caso = 1;
	while(l--){
		unsigned long long r, t;
		cin>>r>>t;
		unsigned long long cont = 0;
		unsigned long long qtd = 0;
		while(1){
			qtd+=(2*r)+1;
			r+=2;
			if(qtd<=t)cont++;
				else break;

		}
		cout<<"Case #"<<caso++<<": "<<cont<<endl;
	}
	

	return 0;
}