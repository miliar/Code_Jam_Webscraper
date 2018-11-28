#include <fstream>
#include <iomanip>
using namespace std;

int main(int argc, char** argv) {
	ifstream ifile(argv[1]);
	ofstream ofile(argv[2]);

	int T; ifile >> T;
	for (int tc = 1; tc <= T; tc++) {
		double c; ifile >> c;
		double f; ifile >> f;
		double x; ifile >> x;

		double time = 0;
		double p = 2;

		double ttw = x / p;
		double ttw_bf = (c / p) + (x / (p + f));
		while (ttw > ttw_bf) {
			time += (c / p);
			p += f;

			ttw = x / p;
			ttw_bf = (c / p) + (x / (p + f));
		}
		time += ttw;

		ofile << "Case #" << fixed << setprecision(7) << tc << ": " << time << endl;
	}

	return 0;
}