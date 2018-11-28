#include<fstream>
using namespace std;

ifstream fin("input.in");
ofstream fout("output.out");

int main() {
	int a, b, k, i, j, t, it, nrsol;
	fin >> t;
	for(it = 1; it <= t; it++) {
		fin >> a >> b >> k;
		nrsol = 0;
		for(i = 0; i < a; i++) {
			for(j = 0; j < b; j++) {
				if((i & j) < k) {
					nrsol++;
				}
			}
		}
		fout << "Case #" << it << ": " << nrsol << "\n";
	}
	return 0;
}
