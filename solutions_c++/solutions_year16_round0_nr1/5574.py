#include <iostream>
#include <bitset>
#include <fstream>
using namespace std;

int main(){
	ifstream datos("datos.txt");
	ofstream salida ("salida.txt");
	bitset<10> bs;
	int t,  N, a,  cont;long long int n;
	datos >> t;
	for(int i=1; i<=t; ++i){
		datos >> N;
		if(N==0) salida <<"Case #" << i << ": "<< "INSOMNIA\n" ;
		else {
		n=N;
		bs.reset();
		cont=0;
		while(cont<10){
			a=n;
			while(a>0){
				if(!bs[a%10]) {
					bs[a%10]=1;
					++cont;
				}
				a/=10;
			}	
			n+=N;
			if(n>10000000000) break;
		}
		salida << "Case #" << i << ": ";
		if(cont==10) salida << n-N ;
		else salida << "INSOMNIA";
		salida << '\n';
		}
	}
	return 0;
}
