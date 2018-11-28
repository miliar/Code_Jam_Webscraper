//#include <iostream>
#include <fstream>
#include <math.h>
#include <cassert>

using namespace std;

ifstream in ("input.txt");
ofstream cout ("output.txt");


void controlla_cifre (int num_cifre, long long int num, bool *digit) {
	long int numero = num;
	for (int i = num_cifre; i>=0; i--) {
		int j = 1;
		while (numero - j*pow(10,i) >= 0) {
			j++;
		}
		j--;
		numero -= j*pow(10,i);
		//cout << "numero= " << num << endl;
		digit [j] = true;
	}
	/*
	for (int i = 0; i <10; i++) {
		cout << digit[i] << "\t" ;
	}
	cout << endl;
	*/
}

int main()
{
	int T;
	in >> T;
	
	for (int q=1; q<=T; q++) {
		long long int N;
		in >> N;
		int num = N;
		bool finito = false;
		if (N == 0) {
			cout << "Case #" << q << ": INSOMNIA" << endl;
		}
		else {
			long int moltiplicatore = 1;
			bool digit[10];
			for (int i=0; i <10; i++) 
				digit[i] = false;
			while (!finito) { // Finché non abbiamo trovato tutti e 10 i numeri
				int num_cifre = 0;
				while (pow (10, num_cifre) <= num) {
					num_cifre++;
				}
				num_cifre--;
				controlla_cifre (num_cifre, num, digit);
				
				finito = true;
				for (int i = 0; i < 10; i++) {
					if (digit[i] == false)
						finito = false;
				}
				if (finito) {
					cout << "Case #" << q << ": " << num << endl; 
				}
				else {
					num = (++moltiplicatore) * N;
				}
			}
		}
	}
	
	return 0;
}

