/*Author: Vasile Mihail-Raul, Romania
  Mail: vasile.raul@webmonsters.ro */

#include <fstream>
#include <iomanip> 

using namespace std;

//PPS = Production per Second
//FPPS = Future production per Second

double solve(double C, double F, double X) {
	double PPS = 2;
	double totalTime = 0;
	while(true) {
		double timeForX = X / PPS; //Time for getting X cookies
		double timeForF = C / PPS; //Time for getting a new farm
		double FPPS = PPS + F; //Future production per second with a new farm
		double newTimeForX = X / FPPS; //New time for getting X cookies, with FPPS

		if(newTimeForX + timeForF > timeForX) {
			totalTime = totalTime + timeForX;
			break;
		} else {
			totalTime = totalTime + timeForF;
			PPS = FPPS;
		}
	}

	return totalTime;
}

int main(int argc, char* argv[]) {

	ifstream in("cookieclicker.in");
	ofstream out("cookieclicker.out");

	int T, noCase = 1;

	in >> T;

	while(T--) {
		double C, F, X;
		
		in >> C >> F >> X;

		double sol = solve(C, F, X);

		//out.setf(fixed);
		out<<"Case #"<<noCase++<<": "<< fixed << setprecision(7) << sol <<"\n";
	}

	return 0;
}//close main
