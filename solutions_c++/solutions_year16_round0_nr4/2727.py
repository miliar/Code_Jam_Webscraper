#include <bits/stdc++.h>
using namespace std;

int main() {
	ifstream fin("inp.txt");
	ofstream fout("out.txt");
	int T; fin >> T;
	for(int cs = 1; cs <= T; cs++) {
		int K, C, S; fin >> K >> C >> S;
		fout << "Case #" << cs << ":";
		for(int i = 1; i <= K; i++) fout << " " << i;
		fout << "\n";
	}
	fout.flush();
}
