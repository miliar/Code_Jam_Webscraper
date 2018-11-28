#include <iostream>
#include <fstream>
using namespace std;

int main () {
	ifstream in("input.txt");
	ofstream out("output.txt");

	int a[4][4];
	
	int n;
	in >> n;
	int c1[4],c2[4];
	int k1 = 0, k2 = 0;
	for (int kk = 0; kk < n; kk++) {
		in >> k1;
		for (int i = 0; i < 4;i++) {
			for (int j = 0; j < 4; j++) {
				in >> a[i][j];
			}
			if (i == (k1-1)) {
				for (int k = 0; k < 4; k++) {
					c1[k] = a[i][k];
				}
			} 
		}
		in >> k2;
		for (int i = 0; i < 4;i++) {
			for (int j = 0; j < 4; j++) {
				in >> a[i][j];
			}
			if (i == (k2-1)) {
				for (int k = 0; k < 4; k++) {
					c2[k] = a[i][k];
				}
			} 
		}
		int counter = 0;
		int ans = 0;
		for(int i = 0; i < 4; i++) {
			for (int j = 0; j< 4;j++) {
				if(c1[i]==c2[j]){
					counter++;
					ans = c1[i];
				}
			}
		}
		if (counter == 1) {
			out << "Case #" << kk + 1<< ": " << ans << endl;
		}
		if (counter > 1 ) {
			out << "Case #" << kk + 1<< ": Bad magician!" << endl;
		}
		if (counter == 0) {
			out << "Case #" << kk + 1<< ": Volunteer cheated!" << endl;
		}		
	}

	return 0;

}
