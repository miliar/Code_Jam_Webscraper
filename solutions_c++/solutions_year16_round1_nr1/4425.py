// Decodificador M.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <stdlib.h>
#include <string.h>
#include <math.h>
using namespace std;
using namespace std;

int ca,kk;
char cad[1020];
int main()
{

	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	kk = 1;
	cin >> ca;
	while (ca--)
	{
		cin >> cad;
		string aux;
		aux = cad[0];
		for (int i = 1; i < strlen(cad); i++)
		{
			if (cad[i] >= aux[0])
				aux = cad[i] + aux;
			else
				aux = aux + cad[i];
		}
		cout <<"Case #"<<kk++<<": "<< aux << endl;
	}
}

