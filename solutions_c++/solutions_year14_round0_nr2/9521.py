#include <fstream>
#include <iomanip>
using namespace std;

ifstream in("infile.txt");
ofstream out("outfile.txt");


int T;

double C, F, X;


double f(double M, double S, double X){
	double wait = (X - M) / S;

	double farmAndWait;
	if(M < C)
		farmAndWait = (C - M) / S + X / (S + F);
	else
		farmAndWait = (X - (M - C)) / (S + F);

	if(farmAndWait > wait)
		return wait;

	double farm;
	if(M < C)
		farm = (C - M) / S + f(0, S + F, X);
	else
		farm = f(M - C, S + F, X);

	return min(farm, wait);
}

int main(){
	in >> T;
	for(int t = 1; t <= T; ++ t){
		in >> C >> F >> X;

		out << "Case #" << t << ": " << setprecision(7) << fixed << f(0, 2, X) << '\n';
	}

	return 0;
}