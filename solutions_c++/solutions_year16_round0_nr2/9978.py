// ConsoleApplication2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;
#include <fstream>

void inversare(char v[], int n) {
	int i;
	for (i = 0; i <= n; i++) {
		if (v[i] == '+') v[i] = '-';
		else if (v[i] == '-') v[i] = '+';
	}
}

int main()
{
	char sir[100];
	int n, i;

	ifstream f("fisier2.in");
	ofstream g("ies2.out");

	f >> n;
	
	for (i = 0; i < n; i++) {
		f >> sir;
		
		int l = strlen(sir), j, nr = 0;
		
		for (j = l-1; j >= 0; j--) {
			if (sir[j] == '-') {
				inversare(sir, j);
				
				nr++;
			}
		}
		g << "Case #"<<i+1<<": "<<nr << "\n";
		

	}

	return 0;
}

