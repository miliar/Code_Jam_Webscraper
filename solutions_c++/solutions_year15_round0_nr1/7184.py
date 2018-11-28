#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;

int T;

int main()
{
	ifstream in("A-large.in");
	ofstream out("output.txt");
	in >> T;
	for (int i = 0; i < T; i++) {
		int S;
		in >> S;
		string arr;
		
		in >> arr;
		int numSoFar = (arr[0]-48);
		int numAdd = 0;
		if (numSoFar < 1) numSoFar = numAdd = 1;

		for (int j = 1; j <= S; j++) {
			if (numSoFar < j && (arr[j]-48>0)) {
				numAdd += (j - numSoFar);
				numSoFar = j + (arr[j]-48);
			}
			else numSoFar += (arr[j] - 48);
		}

		out << "Case #" << (i + 1) << ": " << numAdd << "\n";
		//cout << "Case #" << (i + 1) << ": " << numAdd << "\n";
	}

	return 0;
}