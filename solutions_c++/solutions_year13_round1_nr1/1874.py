#include <fstream>
using namespace std;

int main() {
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	int T;
	fin >> T;
	for (int i(0); i < T; i++) {
		long long rad, ink;
		fin >> rad >> ink;
		rad++;
		long long count(0), sum(0);
		do {
			sum += rad*2 - 1;
			rad+=2;
			count++;
		}while(sum<ink);
		if (sum > ink) count--;
		fout << "Case #" << i+1 << ": " << count << endl;
	}

}