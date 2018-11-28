#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char* argv[]) {
	if( argc != 3 ) {
		cout << "Usage: " << argv[0] << " <input file name> <output file name>" << endl;
		return 1;
	}
	ifstream in(argv[1]);
	if( !in.is_open() ) {
		cout << "Unable to open the file: " << argv[1] << endl;
		return 1;
	}
	ofstream out(argv[2]);
	
	int T;
	in >> T;
	for(int t = 0; t < T; t++) {
		int A,B,K;
		in >> A >> B >> K;
		long count = 0;
		for(int i = 0; i < A; i++) {
			for(int j = 0; j < B; j++) {
				if((i&j) < K) {
					count++;
				}
			}
		}
		out << "Case #" << (t+1) << ": " << count << endl;
	}
}