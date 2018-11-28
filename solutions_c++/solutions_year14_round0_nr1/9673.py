#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

int a[20];
int main(){
	ifstream fin("A-small-attempt0.in");
	ofstream fout("a.out");
	int T, cas, i, j, k, t;
	fin >> T;
	for (cas = 1; cas <= T; cas++){
		memset(a, 0, sizeof(a));
		fin >> k;
		for (i = 1; i <= 4; i++){
			for (j = 1; j <= 4; j++){
				fin >> t;
				if (i == k) a[t]++;
			}
		}
		fin >> k;
		for (i = 1; i <= 4; i++){
			for (j = 1; j <= 4; j++){
				fin >> t;
				if (i == k) a[t]++;
			}
		}
		t = k = 0;
		for (i = 1; i <= 16; i++){
			if (a[i] == 2){
				t++;
				k = i;
			}
		}
		fout << "Case #" << cas << ": ";
		if (t == 0) fout << "Volunteer cheated!" << endl;
		else if (t > 1) fout << "Bad magician!" << endl;
		else fout << k << endl;
	}
	return 0;
}
