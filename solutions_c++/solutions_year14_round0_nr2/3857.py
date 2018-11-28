#include<fstream>
#include<iomanip>
#include<iostream>

using namespace std;

#define		EPS		1e-8

ifstream fin("B-small-attempt0.in");
ofstream fout("B-small-attempt0.out");

int main(){

	cin.rdbuf(fin.rdbuf());
	cout.rdbuf(fout.rdbuf());

	double c,f,x,r;

	int ntc,k;
	cin >> ntc;

	for (int tc=1;tc<=ntc;tc++){
		cout << "Case #" << tc << ": ";
		k = r = 0;
		cin >> c >> f >> x;
		double res;
		do{
			res = r + x/(2+k*f);
			r += c/(2+k*f);
			k++;
		}while(r + x/(2+k*f)<res+EPS);
		cout << fixed << setprecision(7) << res << endl;
	}

	return 0;
}