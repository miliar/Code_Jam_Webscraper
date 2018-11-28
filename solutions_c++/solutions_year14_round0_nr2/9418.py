#include <iostream>
#include <iomanip>
#include <fstream>
#define lim 100000
using namespace std;

int t;
double C, F, X;
double fmin(double a, double b) { if(a < b) return a; return b; }

double solve(int owned, double passedSoFar) {
	//am doua optiuni:
	//1) astept sa se adune X cookies
	//2) cumpar (cand pot) o ferma noua si astept de acolo

	double rate = 2.0 + double(owned) * F;

	double untilX = X / rate;
	double untilFarm = C / rate;

	//in loc sa cumpar toate fermele astea, puteam sa astept la inceput pana aveam X
	if(passedSoFar > (X / 2.0)) return 0.0;	
	if(owned > lim) return 0.0;

	return fmin(untilX, untilFarm + solve(owned+1, passedSoFar + untilFarm));
}

	

int main() {
	ifstream f("cookie_clicker_alpha.in");
	ofstream g("cookie_clicker_alpha.out");

	f>>t;
	for(int T=1; T<=t; T++) {
		f>>C>>F>>X;
		
		g<<fixed;
		g<<"Case #"<<T<<": "<<setprecision(7)<<solve(0, 0.0)<<"\n";
	}

	return 0;
}

