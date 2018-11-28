#include<fstream>
using namespace std;

int main(){
	ifstream f("B-large.in");
	ofstream g("Output");
	int T, i;
	double C, F, X, now, total;
	g.precision(7);
	g.setf(ios::fixed, ios::floatfield);
	f >> T;
	for(i = 0; i < T; ++i){
		total = 0; now = 2;
		f >> C >> F >> X;
		while(X / now > C / now + X / (now + F)){
			total += C / now;
			now += F;
		}
		total += X / now;
		g << "Case #" << i+1 << ": " << total << endl;
	}
	return 0;
}