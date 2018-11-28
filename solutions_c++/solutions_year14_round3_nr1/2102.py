#include <iostream>
#include <fstream>
#include <stdio.h>

using namespace std;
int TC, P, Q, sol=0;

bool isPari(int n) {
	return ( (n%2 == 0) ? true : false);
}

bool is2Pow(int n) {
	while(true) {
		if(n == 2) {
			return true;
		}
		if(n%2 == 0) {
			n = n / 2;
		} else {
			return false;
		}
	}
}

int main(int argc, char **argv)
{
	fstream out;
	FILE *pFileInput;
	pFileInput = fopen("A-small-attempt1.in", "r");
	rewind(pFileInput);
	out.open("output.txt", ios::out);
	fscanf(pFileInput, "%d", &TC);
	
	for(int tc=1; tc<=TC; tc++) {
		// GET DATAS
		fscanf(pFileInput, "%d/%d", &P, &Q);
		
		// SOLVE
		// risolviamo lo small, quindi non c'è bisogno di semplificare
		if(!isPari(Q)) {
			sol = -1;
		} else {
			if(!is2Pow(Q)) {
				sol = -1;
			} else { 
				while(P < Q) {
					sol++;
					Q = Q/2;
				}
			}
		}
		
		out << "Case #" << tc << ": ";
		if(sol == -1)
			out << "impossible";
		else
			out << sol;
			
		out << endl;
		sol = 0;
	}
	
	fcloseall();
	return 0;
}
