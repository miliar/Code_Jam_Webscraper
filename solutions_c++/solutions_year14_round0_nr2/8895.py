#include <fstream>
#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

double funkcja(double C, double X, double curF, double F){
	double wynik = 0;
	
	while ((C / curF) + (X / (curF + F)) < X / curF){
		wynik += C / curF;
		curF += F;
	}
	wynik += X / curF;
	return wynik;
}

int main(){
	fstream plik, plikout;
	plik.open("a.in", ios::in);
	plikout.open("a.out", ios::out);
	int n;
	plik >> n;
	double C, F, X;
	for (int i = 0; i < n; i++){
		plik >> C >> F >> X;
		plikout << setprecision(10) << fixed <<  "Case #" << i + 1 << ": " << funkcja(C, X, 2, F) << endl;
	}
	

	plik.close();
	plikout.close();
}