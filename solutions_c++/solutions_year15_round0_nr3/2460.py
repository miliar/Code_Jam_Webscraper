#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int T, t, L, X;
string str;
int f[4][4] = {0, 1, 2, 3, 1, 0, 3, 2, 2, 3, 0, 1, 3, 2, 1, 0};
int g[4][4] = {1, 1, 1, 1, 1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, -1};

int main() {
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");
	fin >> T;
	t = T;
	while (T--) {
		fin >> L >> X;
		fin >> str;
		bool hasI, hasJ;
		hasI = hasJ = false;
		int sum = 0;
		int flag = 1;
		for (int x=0; x<X; x++) {
			for (int l=0; l<L; l++) {
				flag *= g[sum][str[l]-'i'+1];
				sum = f[sum][str[l]-'i'+1];
				if (flag==1) {
					switch (sum) {
						case 0: 
							break;
						case 1: 
							if (!hasI)
								hasI = true;
							break;
						case 2:
							break;
						case 3:
							if (hasI && !hasJ)
								hasJ = true;
							break;
					}
				}
			}
		}
		fout << "Case #" << t-T << ": ";
		if (flag==-1 && sum==0 && hasJ) {
			fout << "YES" << endl;
		}
		else
			fout << "NO" << endl;
	} 
}
