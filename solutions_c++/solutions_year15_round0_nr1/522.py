// GCJ20150A0.cpp�: d�finit le point d'entr�e pour l'application console.
//

#include "stdafx.h"
// Ci-dessous pour ne plus �tre g�n� par les erreur de compilation
// d�es � scanf, strcpy, etc...
// sans pour autant � chaque fois devoir red�finir _CRT_SECURE_NO_WARNINGS
// dans la d�finition du pr�processseur (Projet>Propri�t�s>Conf>C/C++>Pr�processeur/D�finitions)
#pragma warning(disable: 4996) /* Disable deprecation */

#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <ctime>
#include <algorithm>
#include <string.h>

using namespace std;

class Perf
{
public:



	void PerformLoop()
	{
		int i, j, k, som, tmp;
		char in[10000];
		char LOut[10000];
		int Res;

		// Sp�cifique
		int nshy,nb;
		vector <int> Shy;

		// D�but d'analyse
		// Init
		Res = 0;

		// Extraction
		// Combinaisons
		*FicIn >> nshy;
		*FicIn >> in;
		for (i = 0; i <= nshy; i++)
		{
			Shy.push_back((int)(in[i]-'0'));
		}

		// Ex�cution
		// V�rification :  chaque bit 1 doit �tre en nombre pair
		if (Shy[0] == 0) Res++;
		nb = Res + Shy[0];
		for (i = 1; i <= nshy; i++)
		{
			if (nb < i)
			{
				Res += i - nb;
				nb += i - nb;
			}
			nb += Shy[i];
		}

		// Formatage de la sortie

		// Sortie
		sprintf(LOut, "Case #%d: %d\n", Nt,Res);
		printf("%s", LOut);
		*FicOut << LOut;
	}

	void Perform()
	{
		// Ouverture des fichiers
		FicIn = new fstream("A-large.in", ifstream::in);
		FicOut = new fstream("Fichier.out", ifstream::out);

		// Nombre de Tests
		*FicIn >> T;

		for (Nt = 1; Nt <= T; Nt++) PerformLoop();

		// Fermeture des fichiers
		FicIn->close();
		FicOut->close();
	}

	int T, Nt;
	fstream *FicIn;
	fstream *FicOut;


};

int main(int argc, char** argv)
{
	Perf P;

	printf("GCJ20150A0\n");
	P.Perform();

	return 0;
}