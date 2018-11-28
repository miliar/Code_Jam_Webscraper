#include <iostream>
#include <fstream>

using namespace std;

int do_case(int*, int);

int main() {
	ofstream fout;
	fout.open("file.out");
	ifstream fin;
	fin.open("A-large.in");
	//fin.open("A-small-attempt1.in");
	//fin.open("file.in");

	int T;
	fin >> T;


	for (int i = 0; i<T; i++) {
		int k = 0;
		fin >> k;
		fin.get();
		int* audience = new int[k];
		for (int j = 0; j <= k; j++) {
			audience[j] = fin.get() - '0';
		}
		fout << "Case #" << (i + 1) << ": " << do_case(audience, k) << endl;
	}
	fout.close();
	fin.close();
	return 0;
}


int do_case(int* audience, int k) {
	int standing = 0;
	int added = 0;
	for (int i = 0; i <= k; i++) {
		while (i > standing) {
			added++;
			standing++;
		}
		standing += audience[i];
	}
	return added;
}
