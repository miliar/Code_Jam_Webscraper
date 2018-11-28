#include <fstream>
#include <iomanip>
using namespace std;
int main(){
	ifstream fin("B-large.in");
	ofstream fout("b.out");
	int T;
	double c, f, x;
	fin>>T;
	for (int n = 0; n < T; ++n){
		fin>>c>>f>>x;
		double t = 0, s = 2, ff, nf;
		while (1){
			ff = c/s+x/(s+f);
			nf = x/s;
			if (ff < nf){
				t += c/s;
				s += f;
			}
			else{
				t += nf;
				break;
			}
		}
		fout<<"Case #"<<n+1<<": "<<fixed<<setprecision(7)<<t<<endl;
	}
	return 0;
}