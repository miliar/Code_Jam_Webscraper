// Rotate.cpp : Defines the entry point for the console application.
//
// wczytywanie
// sortowanie( przepychanie kropek, grawitacja)
// czytanie w sposób odwrócony i szukanie rozwi¹zañ

#include "stdafx.h"
#include <iostream>
#include <fstream>


using namespace std;

class Problem {
private:
	bool tablica[10];
public:
	Problem(long int n, int ktory, ofstream& g) {
		int suma = 0;
		long int temp = 0;
		long int stary = 0;
		long int k = n;
		bool ok = true;
		for (int i = 0; i < 10; i++)
			tablica[i] = false;
		while (suma < 10 && ok) {
			temp = k;
			while (temp > 0) {
				if (!tablica[(temp % 10)]) {
					suma++;
					tablica[(temp % 10)] = true;
				}
					
				temp = temp / 10;
			}
			stary = k;
			k += n;
			if (stary == k)
				ok = false;
		}
		if (ok) g << "Case #" << ktory << ": " << stary << endl;
		else g << "Case #" << ktory << ": INSOMNIA" << endl;
	}

};

int main()
{
	ifstream f;
	ofstream g;
	int problems = 0;
	Problem* p;
	long int n = 0, k = 0;
	f.open("A-large.in");
	g.open("Answer.out");

	f >> problems;
	for (int i = 0; i < problems; i++) {
		f >> n;
		p = new Problem(n, i + 1, g);
		delete p;
	}
	f.close();
	g.close();
	return 0;
}

