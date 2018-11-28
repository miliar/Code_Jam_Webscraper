#include <fstream>
#include <iomanip>
using namespace std;


double C, F, X;
int T;

inline double rate(int nfarm){
	return 2 + nfarm * F;
}

int main(int argc, char** argv){
	if (argc != 3)
		return -1;
	
	ifstream ifs;
	ifs.open(argv[1]);

	ofstream ofs;
	ofs.open(argv[2]);

	ifs >> T;
	for (int i = 0; i < T; i++){
		ifs >> C >> F >> X;

		int nfarm = 0;
		double t = 0;
		while (X / rate(nfarm) > C / rate(nfarm) + X / rate(nfarm + 1)){
			t += C / rate(nfarm);
			nfarm++;
		}
		t += X / rate(nfarm);

		ofs << "Case #" << (i + 1) << ": " << setprecision(10) << t << endl;
	}

	ifs.close();
	ofs.close();
}

