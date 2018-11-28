#include <iostream>
#include <iomanip>

using namespace std;

int main(){

	int T; cin >> T;

	cout << fixed << setprecision(7);

	for (int t = 1; t != T+1; t++){
		cout << "Case #" << t << ": ";
			
		double C, F, X;
		cin >> C >> F >> X;
//cout << C << '\t' << F << '\t' << X << '\n';
		
		double t0 = 0;
		double dc = 2;
		
		double r, s = t0 + X/dc;
		
//cout << s << endl;
		do {
		r = s;
		t0 += C / dc;
		dc += F;
		s = t0 + X/dc;
//cout << s << endl;
		} while (r > s);
		
		cout << r << endl;


	}

	return 0;
}
