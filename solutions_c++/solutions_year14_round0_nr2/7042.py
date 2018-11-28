#include <iostream>
#include <string>
#include <vector>
#include <math.h>


using namespace std;


void dPause() {
	int j = 0;
	++j;
	return;
}


double getTime(double u_C, double u_F, double u_X) {
	double mfloat = u_X / u_C - 2. / u_F - 1.;
	double t0 = 0., t1 = 0., t2 = 0.;
	double t = 0;

	if(mfloat < 2.) {
		t0 = u_X * 0.5;
		t1 = u_C * 0.5 + u_X / (2. + u_F);
		t2 = u_C * 0.5 + u_C / (2. + u_F) + u_X / (2. + 2. * u_F);
		double tmp_t = u_C * 0.5 + u_C / (2. + u_F) + u_C / (2. + 2. * u_F) + u_X / (2. + 3. * u_F);
		t = t0;
		if(t > t1)
			t = t1;
		if(t > t2)
			t = t2;
		if(t > tmp_t)
			t = tmp_t;
		return t;
	}

	double tmp_sum = 0;
	unsigned m0;
	for(m0 = 0; (double)m0 < mfloat - 1.; ++m0) {
		tmp_sum += 1. / (2. + m0 * u_F);
	}
	tmp_sum *= u_C;
	t0 = tmp_sum + u_X / (2. + m0 * u_F);
	t1 = tmp_sum + u_C / (2. + m0 * u_F) + u_X / (2. + (m0 + 1.) * u_F);
	t2 = tmp_sum + u_C / (2. + m0 * u_F) + u_C / (2. + (m0 + 1.) * u_F) + u_X / (2. + (m0 + 2.) * u_F);

	t = t0;
	if(t > t1)
		t = t1;
	if(t > t2)
		t = t2;
	return t;
}






void printResult(int ti, double t) {
//	cout << "Case #" << ti << ": " << t << endl;
	printf("Case #%d: %.7f\n", ti, t);
}




int main()
{
	freopen("B-large.in", "rt", stdin);
	freopen("out-B-large.txt", "wt", stdout);
//	cout.precision(7);
	
	string readLine;

	// Number of tests
	unsigned T;
//	getline(cin, readLine);
//	T = atof(readLine.c_str());
	cin >> T;
	
	for(int ti = 1; ti <= T; ++ti) {
		double C, F, X;
		cin >> C >> F >> X;
		double t = getTime(C, F, X);
		printResult(ti, t);
		dPause();
	}


	dPause();
	return 0;
}