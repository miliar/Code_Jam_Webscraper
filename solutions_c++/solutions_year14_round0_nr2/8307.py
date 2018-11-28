#include<fstream>
#include<iomanip>
using namespace std;

int main(void){
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in", ios_base::in);
	fout.open("B-large.out", ios_base::trunc);
	int T;
	fin >> T;
	for(int c = 1; c <= T; c++){
		double C, F, X;
		fin >> C >> F >> X;
		int N = (int)(X / C - 2 / F);
		if(N < 0)
			N = 0;
		double totalTime = X / (2 + N * F);
		if(N >= 1){
			for(int i = N - 1; i >= 0; i--)
				totalTime += C / (2 + i * F);
		}
		fout.setf(ios::fixed);
		fout.precision(7);
		fout << "Case #" << c << ": " << totalTime << endl;
 	}
	return 0;
}
