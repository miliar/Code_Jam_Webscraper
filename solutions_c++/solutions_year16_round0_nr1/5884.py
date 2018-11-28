#include <iostream>
#include <fstream>
using namespace std;

int main(){
	ifstream infile;
	infile.open("A-large.in");
	if (!infile.is_open()) cout << "Failed to load file!" << endl;

	ofstream outfile;
	outfile.open("output1.txt");
	int T, N;
	infile >> T;

	for (int i = 1; i <= T; i++){
		infile >> N;
		if (N == 0) outfile << "Case #" << i << ": INSOMNIA" << endl;
		else {
			bool a[10] = { false, false, false, false, false, false, false, false, false, false }, flag = false;
			int n, j = 1, d, m;
			while (!flag){
				m = j*N;
				n = m;
				while (n != 0){
					d = n % 10;
					n /= 10;
					if (a[d] != true) a[d] = true;
				}
				d = 0;
				do {
					flag = a[d];
					d++;
				} while (flag == true && d < 10);
				j++;
			}
			outfile << "Case #" << i << ": " << m << endl;
		}
	}
	infile.close();
	outfile.close();
	system("pause");
	return 0;
}