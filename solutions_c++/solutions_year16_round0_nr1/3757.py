#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>

using namespace std;

int main(int argc, char *argv[]) {
	fstream infile, outfile;
	infile.open("A-large.in", ios::in);
	outfile.open("tmp.out", ios::out);
	int t;
	infile >> t;
	for (int kk = 1; kk <= t; kk++) {
		int n;
		int ans = 1;
		bool check[10] = {0};
		infile >> n;
		if (n == 0) {
			outfile << "Case #" << kk <<": "<< "INSOMNIA" << endl;
			continue;
		}
		bool tap = true;
		//
		while (true) {
			int tmp = n * ans;
			string tmpn = to_string(tmp);
			// change
			for (int i = 0; i < tmpn.length(); i++) {
				check[tmpn[i] - '0'] = 1;
			}
			// check
			bool flag = 1;
			for (int i = 0; i < 10; i++) {
				if (check[i] == 0) {
					flag = 1;
					break;
				}
				if (i == 9) {
					flag = 0;
					break;
				}
			}
			if (!flag) break;
			if (ans > 10000000) {
				tap = false;
				break;
			}
			//
			ans++;
		}
		if (tap) outfile << "Case #" << kk <<": "<<ans * n << endl;
		else outfile << "Case #" << kk <<": "<< "INSOMNIA" << endl;
	}
	infile.close();
	outfile.close();
	return 0;
}