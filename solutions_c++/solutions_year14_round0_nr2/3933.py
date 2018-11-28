#include<iostream>
#include<vector>
#include<fstream>
#include<iomanip>
using namespace std;
int main() {
	ifstream cin("first.txt");
	double farmrate;
	double increment;
	double required;
	double rate = 2.0;
	double time = 0.0;
	double loops;
	cin >> loops;
	for(int i = 1; i <= loops; i++) {
			cin >> farmrate >> increment >> required;
			if(required <= farmrate) {
				time = required / 2;
			}else {
				while(required / rate > (farmrate / rate) + (required / (rate + increment))) {
					time = time + farmrate / rate;
					rate = rate + increment;
				}
				time = time + (required / rate);
			}
			cout << "Case #" << i << ": " << setprecision(9) << time << endl;
			time = 0.0;
			rate = 2.0;
	}
}