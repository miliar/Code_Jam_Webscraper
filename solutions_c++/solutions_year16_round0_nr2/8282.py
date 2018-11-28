

//#include <iostream>
#include <fstream>
//#include <cassert>
using namespace std;

ifstream in ("input.txt");
ofstream cout ("output.txt");

int main()
{
	int T;
	in >> T;
	for (int q = 1; q<=T; q++) {
		cout << "Case #" << q << ": " ;
		string caratteri;
		in >> caratteri;
		bool car[101];
		for (int i = 0; i<101; i++) {      // Assolutamente inutile.
			car[i] = false;
		}
		int cont1 = 0;
		int cont2 = 1;
		(caratteri[0]=='+')?car[0] = true: car[0] = false; 
		//cout << car[0] <<"\t" ;
		while (caratteri[cont1] != '\0') {
			cont1++;
		}
		
		for (int i = 1; i <cont1; i++) {
			if (caratteri[i] != caratteri[i-1]) {
				(caratteri[i]=='+')?car[cont2++] = true: car[cont2++] = false; 
				//cout << car[cont2-1] << "\t" ;
			}
		}
		bool memoria = car[0];
		for (int i = 0; i < cont2-1; i++) {
			(memoria)?memoria=false:memoria=true;
		}
		if (memoria)
			cout << cont2-1;
		else
			cout << cont2;
		
		cout <<  endl;
	}
	return 0;
}

