//============================================================================
// Name        : TheRepeater.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string.h>
#include <math.h>
#include <stdlib.h>
using namespace std;

int buscarpatron(string s, char patron[101], int potencias[101])
{
	int i = 0, j = 0;
	while (j < s.size())
	{
		patron[i] = s[j];
		potencias[i] = 0;
		while (s[j] == patron[i])
		{
			potencias[i]++;
			j++;
		}
		i++;
	}
	return i;
}



int main() {
	int casos;
	cin >> casos;
	for (int caso = 1; caso <= casos; caso++)
	{
		int n;
		cin >> n;

		string s;
		char patron[101][101];
		for (int i = 1; i<=100;i++)
			memset(patron[i], '\0', sizeof(patron[i]));

		int potencias[101][101];

		cin >> s;

		buscarpatron(s, patron[1], potencias[1]);

		bool ok = true;

		for (int i=2; i<=n ;i++)
		{
			cin >> s;
			buscarpatron(s, patron[i], potencias[i]);

			if (strcmp(patron[i], patron[1]))
			{
				ok = false;
				break;
				//cout << "error" << endl;
			}
//			cout << patron[i] << endl;
//			for (int j=0; j<strlen(patron[i]); j++)
//				cout << potencias[i][j];
//			cout << endl;
		}

		cout << "Case #" << caso << ": ";
		if (!ok)
			cout << "Fegla Won" << endl;
		else
		{
			int cambios = 0;
			for (int i = 0; i<strlen(patron[1]); i++)
			{
				int total = 0;
				for (int j = 1; j <= n; j++)
				{
					total += potencias[j][i];
				}

	//			cout << i << endl;
	//			cout << "total: " << total << endl;
				int media = round((float)total / n);

	//			cout << "media: " << media << endl;

				int desvtotal = 0;
				for (int j = 1; j<=n; j++)
				{
					int desv = abs(media - potencias[j][i]);
					//cout << desv << endl;
					desvtotal += desv;
				}

				cambios += desvtotal;
			}


			cout << cambios << endl;
		}
	}
	return 0;
}
