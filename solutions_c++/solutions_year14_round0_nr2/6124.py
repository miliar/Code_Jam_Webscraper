#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

double C,F,X;

double Solve () {
	
	//cout << setprecision(17);
	double time1 = X/2.000000000;
	double min_time = time1;
	double time2 = X/(F+2.00000000) + C/2.00000000;
	double val = C/2.00000000;
	if ( time2 < min_time ) min_time = time2;
	//cout << min_time << endl;
	//if ( time1 < time2 ) return time1;
	
	int L = 1;

	while ( time1 > time2 ) {

		//float tmp = time2 - X/(L*F+2.0000000);
		//cout << "tmp & L " << tmp << " " << L << endl;
		L++;
		val = val + C/((L-1)*F+2.000000);
		double tmp = X/(L*F+2.000000)+val;
		//cout << tmp << endl;
		time1 = time2;
		time2 = tmp;
		if ( time2 < min_time) min_time = time2;
	}

	return min_time;

}
void Readata() {

	int T;
	cin >> T;
	//double C,F,X;
	for ( int i = 0 ; i < T; i++ ) {
		cin >> C >> F >> X;
		std::cout << std::fixed << std::setprecision(7);
		//cout.precision(7);
		cout << "Case #" << i+1 << ": " << Solve() << endl;
	}
}

int main()
{
	Readata();
	return 0;
}
