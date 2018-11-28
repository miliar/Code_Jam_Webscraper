#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <bitset>
#include <string>
#include <cmath>


using namespace std;

ifstream in ("in.txt");
ofstream out ("out.txt");

int K, C, S;

typedef long long ll;


int main() {

	int T; in >> T;

	for (int i = 1; i <= T; i++) {

		in >> K >> C >> S;
			
			out << "Case #" << i << ": ";
			for (int j = 1; j <= K-1; j++) {
				out << j << " ";
			}
			out << K << endl;

	}


	in.close();
	out.close();
	return 0;
}
