#include <fstream>
#include <iostream>

using namespace std;

int main() {
	ifstream fin("B-small-attempt0.in");
	ofstream fout("B-B-small-attempt0.out");
	int cases;
	int i,j;
	int A, B, K;
	int count;
	string tmp_str;

	fin >> cases;
	for(i = 0; i < cases; ++i) {
		count = 0;
		fin >> A >> B >> K;
		for(int a = 0; a < A; ++a) {
			for(int b = 0; b < B; ++b) {
				if((a&b) < K) {
					count++;
				}
			}
		}
		
		fout << "Case #" << i+1 << ": " << count << endl;
	}

	fin.close();
	fout.close();
}