#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <fstream>
#include <string>

using namespace std;
ifstream cin ("input.txt");
ofstream cout ("output.txt");


int main()
{
	int t;     // è il numero di casi da analizzare;
	cin >> t;
	for (int q = 0; q < t; q++) {               // Fai l'algoritmo per un numero t di volte, cioè i casi da fare.
		int s;                      // è il numero massimo di livello di timidezza.
		string persone;             // è la stringa che contiene le persone con timidezza [i].
		cin >> s;
		cin >> persone;
		int in_piedi = (int)persone[0] - '0';
		int amici = 0;
		int i = 1;
		while (persone[i] != '\0') {
			if (i <= in_piedi) {           // Se possono alzarsi le persone
				in_piedi += (int)persone[i] - '0';
			}
			else if (i > in_piedi)              // Se non possono alzarsi in piedi
			{
				amici += i - in_piedi;
				in_piedi += (int) persone [i] - '0' + i - in_piedi;;
			}
			i++;
		}
		cout << "Case #" << q+1 << ": " << amici << endl;
	}
}
