#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
#include <cmath>
#include <string>
#include <fstream>
using namespace std;

#define sol(i) salida << "Case #" << i << ": ";

int main(){
	ifstream datos("entrada.txt");
	ofstream salida("salida.txt");
	int casos;char aux;
	datos >> casos; datos.get(aux);
	for (int C = 1; C <= casos; ++C){
		vector<int> v(100, 0), solu(10, 0);  int n;
		datos.get(aux);
		while (aux != '\n'){
			v[int(aux)]++;
			datos.get(aux);
		}

		n = solu[0] = v[int('Z')];
		if (n){ v[int('Z')] -= n; v[int('E')] -= n; v[int('R')] -= n; v[int('O')] -= n; }
		n = solu[2] = v[int('W')];
		if (n){ v[int('T')] -= n; v[int('W')] -= n; v[int('O')] -= n; }
		n=solu[6] = v[int('X')];
		if (n){ v[int('S')] -= n; v[int('I')] -= n; v[int('X')] -= n; }
		n= solu[8] = v[int('G')];
		if (n){ v[int('E')] -= n; v[int('I')] -= n; v[int('G')] -= n; v[int('H')] -= n; v[int('T')] -= n; }
		n= solu[7] = v[int('S')];
		if (n){ v[int('S')] -= n; v[int('E')] -= n; v[int('V')] -= n; v[int('E')] -= n; v[int('N')] -= n; }
		n= solu[5] = v[int('V')];
		if (n){ v[int('F')] -= n; v[int('I')] -= n; v[int('V')] -= n; v[int('E')] -= n; }
		n= solu[4] = v[int('F')];
		if (n){ v[int('F')] -= n; v[int('O')] -= n; v[int('U')] -= n; v[int('R')] -= n; }
		n= solu[3] = v[int('R')];
		if (n){ v[int('T')] -= n; v[int('H')] -= n; v[int('R')] -= n; v[int('E')] -= n; v[int('E')] -= n; }
		n= solu[1] = v[int('O')];
		if (n){ v[int('O')] -= n; v[int('N')] -= n; v[int('E')] -= n; }
		n= solu[9] = v[int('E')];
		sol(C);
		for (int i = 0; i < 10; ++i)
			for (int j = 0; j < solu[i]; ++j)
				salida << i;
		salida << '\n';



	}

	return 0;
}