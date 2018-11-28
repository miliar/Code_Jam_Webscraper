#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string.h>
using namespace std;

void print_arr(bool arr[], int size) {
	for (int i=0; i<size; i++) {
		//cout << arr[i];
	}
	//cout << endl;
}

int main(int argc, char *argv[]) {
	string ipfn,opfn;
	ifstream ipfs;
	ofstream opfs;

	//cout << "Have " << argc << " arguments:" << endl;
	for (int i=0; i<argc; i++) {
		//cout << "argv[" << i << "]: "<<  argv[i] << endl;
	}
	ipfn = argv[1]; 
	ipfs.open(ipfn.c_str());

	opfn = argv[2]; 
	opfs.open(opfn.c_str());

	string line;
	getline(ipfs, line);

	int T;
	T = atoi(line.c_str());

	int cn=1;
	char ic;
	while (cn <=T && ipfs.peek() != EOF) {
		getline(ipfs, line);
		//cout << "READ:" << line << endl;
		int sp = line.find(" ");
		string ps;
		int k;
		ps = line.substr(0,sp);
		k = atoi(line.substr(sp+1).c_str());
		//cout << "PANCAKES:" << ps << " K:" << k << endl;
		int pancake_size = ps.length();
		bool arr[pancake_size];
		for (int i=0; i<ps.length(); i++) {
			char a = ps[i];
			if (a == '-') arr[i] = 0;
			else arr[i] = 1;
		}
		print_arr(arr, pancake_size);
		int cnt = 0;
		for (int i=0; i<=pancake_size-k; i++) {
			if (arr[i] == 0) {
				// FLIP
				cnt++;
				for (int n=0; n<k; n++) {
					arr[i+n] = !arr[i+n];
				}
			}
			print_arr(arr, pancake_size);
		}
		// Check if any nonflipped ones left
		int done=1;
		for (int i=pancake_size-k+1; i<pancake_size; i++) {
			if (arr[i] == 0) {
				done=0;
				break;
			}
		}

		// Result
		opfs << "Case #" << cn << ": ";
		if (done) {
			opfs << cnt << endl;
		} else {
			opfs << "IMPOSSIBLE" << endl;
		}
		cn++;
	}

}
