#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>

using namespace std;

int main() {
    int numCases;
    
    ifstream infile("A-small-attempt0.in");
    infile >> numCases;
    int count = 0;

    while (count < numCases) {
        int sMax;
        infile >> sMax;

        int result = 0;
        string str;
        int curr, sum = 0;
        infile >> str;

		for (int i = 0; i <= sMax; i++) {
			curr = str.at(i) - '0';
			if (curr != 0) {
				if (sum < i) {
					result += i - sum;
					sum += result;
				}
				sum += curr;
			}
		}

        count++;
        cout << "Case #" << count << ": " << result << endl;
    }
 
    return 0;
}
