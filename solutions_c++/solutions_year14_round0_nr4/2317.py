/*Author: Vasile Mihail-Raul, Romania
  Mail: vasile.raul@webmonsters.ro */

#include <fstream>
#include <algorithm>
#include <iomanip> 

using namespace std;

int solveWar(int N, double Kevin[1000], double Naomi[1000]) {
	int points = 0;
	int Nend = N - 1, Kend = N - 1, Nbegin = 0, Kbegin = 0;
	
	while(Nend >= Nbegin && Kend >= Kbegin) {
		if(Naomi[Nend] > Kevin[Kend]) {
			Nend--;
			Kbegin++;
			points++;
		} else {
			Nend--;
			Kend--;
		}
	}
	return points;
}

int solveDec(int N, double Kevin[1000], double Naomi[1000]) {
	int points = 0;
	int Nend = N - 1, Kend = N - 1, Nbegin = 0, Kbegin = 0;

	while(Nend >= Nbegin && Kend >= Kbegin) {
		if(Naomi[Nbegin] < Kevin[Kbegin]) {
			Kend--;
			Nbegin++;
		} else {
			Nbegin++;
			Kbegin++;
			points++;
		}
	}
	return points;
}

void reading(ifstream &in, int &N, double Kevin[1000], double Naomi[1000]) {
	in >> N;
	for(int i = 0 ; i < N ; i++) {
		in >> Naomi[i];
	}
	sort(Naomi, Naomi + N);
	for(int i = 0 ; i < N ; i++) {
		in >> Kevin[i];
	}
	sort(Kevin, Kevin + N);
}

int main(int argc, char* argv[]) {

	ifstream in("deceitfulwar.in");
	ofstream out("deceitfulwar.out");

	int T, noCase = 1;

	in >> T;

	while(T--) {
		int N;
		double Kevin[1000], Naomi[1000];
		reading(in, N, Kevin, Naomi);

		/*out<<"Naomi: ";
		for(int i = 0 ; i < N ; i++)
			out<<fixed<<setprecision(3)<<Naomi[i]<<" ";
		out<<"\n";
		out<<"Kevin: ";
		for(int i = 0 ; i < N ; i++)

		out<<"\n\n";*/

		out << "Case #" << noCase++ << ": " << solveDec(N, Kevin, Naomi);
		out << " " << solveWar(N, Kevin, Naomi) << "\n";
	}

	return 0;
}