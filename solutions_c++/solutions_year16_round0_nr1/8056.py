#include<iostream>
#include<fstream>
using namespace std;
int main() {
	ifstream openfile;
	fstream outfile;
	openfile.open("A-large.in");
	outfile.open("1.out", ios::out);

	int T, N;
	openfile >> T;
	for (int cases = 1; cases <= T; cases++) {
		outfile << "Case #" << cases << ": ";
		int ans = 0;
		openfile >> N;
		if (N == 0) { outfile << "INSOMNIA" << endl; continue; }
		for (int i = 1; ans != 1023; i++) {
			for (int temp = i*N; temp != 0; temp /= 10) {
				ans |= 1 << (temp % 10);
				if (ans == 1023) {
					outfile << i*N << endl;
					break;
				}
			}
		}
	}
	openfile.close();
	return 0;
}
