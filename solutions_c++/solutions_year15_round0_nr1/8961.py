#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstdio>
using namespace std;

int main() {
	string cadena;	
	unsigned T, smax, faltan, total;
	
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);	
	
	cin >> T;
	
	for (int j=1; j<=T; j++){
		total=0;
		cin >> smax >> cadena;

		unsigned sumaaplaudidores=cadena[0]-48;
		
		for (int i=1; i<cadena.size(); i++){
			if ( i > sumaaplaudidores  && ((cadena[i]-48) > 0) ) {
				faltan = i - sumaaplaudidores;
				sumaaplaudidores+= faltan;
				total+= faltan;
			}
			sumaaplaudidores += (cadena[i]-48);
		}
		cout << "Case #" << j << ": " << total << endl;
	}
	//system("pause");
	return 0;
}

