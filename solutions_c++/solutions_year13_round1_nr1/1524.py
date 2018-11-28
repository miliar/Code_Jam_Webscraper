#include "stdafx.h"
#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;

int main(int argc, char* argv[])
{
    ifstream sourceFile("./A-small-attempt0.in");
    ofstream output("./output.txt");

    int T;
    sourceFile >> T;

	for(int i = 0; i < T; i++) {
		int r, t;
		sourceFile >> r >> t;

		int result = 0;
		
		do {
			int square = pow(r + 1, 2) - pow(r, 2);
			t -= square;
			
			if(t >= 0) {
				result++;
			}

			r += 2;
		} 
		while (t > 0);
		output << "Case #" << i + 1 << ": " << result << endl;
	}

	cin >> T;
    return 0;
}