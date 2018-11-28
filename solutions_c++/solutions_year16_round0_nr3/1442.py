

#include "stdafx.h"
#include <iostream>
#include <fstream>


using namespace std;

class Problem {
private: int tablica[32];
		 int rozmiar;
		 int cel;
		 int udanych = 0;
		 int dzielniki[9];
		 ofstream&g;
public:
	void wypisz() {
		for (int i = rozmiar - 1; i >= 0; i--)
			g << tablica[i];
		g << " ";
		for (int i = 0; i < 9; i++)
			g << dzielniki[i] << " ";
		g << endl;
	}
	bool sprawdz(int baza) {
		int dzielnik = 2;
		bool zrobione = false;
		int index = rozmiar - 1;
		int liczba = 0;

		while (dzielnik < pow(baza,rozmiar-1)&& dzielnik <80000 && !zrobione) {
			if (dzielnik%baza == 0) {
				dzielnik++;
				continue;
			}
			liczba = 0;
			for (int index = rozmiar - 1; index >= 0; index--) {
				liczba *= baza;
				liczba += tablica[index];
				liczba = liczba % dzielnik;
			}
			if (liczba == 0) {
				zrobione = true;
				dzielniki[baza - 2] = dzielnik;
			}
			else dzielnik++;
		}
		return zrobione;
	}
	void rekurencja(int index) {
		bool ok = true;
		int i = 2;
		if (index == 0) {
			while (ok && i <= 10) {
				ok = sprawdz(i);
				i++;
			}
			if (ok) {
				udanych++;
				wypisz();
				if (udanych == cel) return;
			}
		}
		else {
			if (udanych == cel) return;
			tablica[index] = 0;
			rekurencja(index - 1);
			if (udanych == cel) return;
			tablica[index] = 1;
			rekurencja(index - 1);
		}
	}
	Problem(int a, int b, ofstream& k)
		:g(k)
	{
		g << "Case #1: "<<endl;
		rozmiar = a;
		cel = b;
		cout << rozmiar << cel << endl;
		tablica[0] = 1;
		tablica[rozmiar - 1] = 1;
		rekurencja(rozmiar - 2);

	}

};

int main()
{
	ifstream f;
	ofstream g;
	int problems = 0;
	Problem* p;
	string stos = "";
	long int n = 0, k = 0;
	f.open("A-small-problem.in");
	g.open("Answer.out");

	f >> problems;
	for (int i = 0; i < problems; i++) {
		f >> n;
		f >> k;
		p = new Problem(n, k, g);
		delete p;
	}
	f.close();
	g.close();
	return 0;
}

