#include <iostream>
#include <iomanip>
#include <cstdlib>

using namespace std;

int main() {
	int t, tnumber = 1;
	double c, f, x;
	double ntime, ptime, farmTime;
	double cookieSpeed;
	
	cin >> t;
	
	while (t--) {
		cin >> c >> f >> x;
		cookieSpeed = 2.0;
		
		ptime = x / cookieSpeed;
		ntime = 0;
		farmTime = 0;
		
		while (ptime>=ntime) {
			farmTime += (c / cookieSpeed);
			cookieSpeed += f;
			
			if (ntime!=0) {
				ptime = ntime;
			}
			
			ntime = farmTime + (x / cookieSpeed);
			
		}
		
		cout << "Case #" << setprecision(7) << std::fixed << tnumber++ << ": " << ptime << "\n";
		
	}
}
