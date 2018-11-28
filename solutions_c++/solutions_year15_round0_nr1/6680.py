#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

#define SMAX 1001

ifstream fin("a.in");
ofstream fout("a.out");

int Smax;
int s[SMAX];

int minguests() {

	int n=0, m =0;
	for(int i=0; i<=Smax; i++) {
		if(m<i) {
			n += (i-m);
			m = i;
		}
		m += s[i];
	}

	return n;

}


int main() {

	int T; fin>>T;
	for(int t=1; t<=T; t++) {

		fin >> Smax;
		for(int i=0; i<=Smax; i++) {
			char ch; fin>>ch;
			s[i] = (int)(ch-'0');
		}

		int n = minguests();

		fout << "Case #" << t << ": " << n << endl;
	}

	return 0;
}

