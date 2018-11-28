#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;
void calc (double C, float F, float X) {

	int trial = 0;
	double step=2;
	double nt, pt;
	double rec = 0;
	nt = 0;
	pt = 0;

	if (C >= X) {
		cout<<setprecision(10)<<(X/step)<<endl;
		return;
	}

	rec = C/step;
	pt = X/step;

	while(1) {
		nt = (X/(F +step))+(rec);	
		if (pt <= nt) {
			cout<<setprecision(10)<<pt<<endl;
			return;
		}
		step += F;
		rec += C/step;
		pt = nt;
	}
}


int main() {
	fstream f;
	f.open("a.dat",ios::in);
	if (!f.is_open()) {
		throw "Failed to open input";
	}

	int N;
	double F,X,C;

	f>>N;

	for (int i = 1; i<=N; i++) {
		cout<<"Case #"<<i<<": ";
		f>>C>>F>>X;

		calc(C,F,X);
	}
	return 0;
}
