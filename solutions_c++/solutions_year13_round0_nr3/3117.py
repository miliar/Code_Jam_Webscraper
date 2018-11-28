#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <string>

using namespace std;

bool isPalindrome(int x) {
    vector<int> v;
    bool palindrome = true;

    while (x != 0) {
        v.push_back(x%10);
        x = x/10;
    }
    int i = 0;
    while (i < (v.size()/2) and palindrome) {
        palindrome = v[i] == v[v.size()-i-1];
        i++;
    }
    return palindrome;
}

void readInput(const char *fileName, vector<int> &v) {
	ifstream in_file;
    int nCases, min, max, square, result;


	in_file.open(fileName, ifstream::in);
	if (in_file.fail()) cout << "**Opening file error**" << endl;
	else {
		in_file >> nCases;
		for (int i = 0; i < nCases; i++) {
            in_file >> min;
            in_file >> max;
            result = 0;
            for (int j = min; j <= max; j++) {
                if (isPalindrome(j)) {
                    square = (int)sqrt(j);
                    if (square*square == j) {
                        if (isPalindrome(square)) result++;
                    }
                }
            }
            v.push_back(result);
		}
		in_file.close();
	}
}

void writeOutput(const char *fileName, vector<int> &v) {
	ofstream out_file;

	out_file.open(fileName, ofstream::out);
	if (out_file.fail()) cout << "**Opening file error**" << endl;
	else {
        for (int i = 0; i < v.size(); i++) out_file << "Case #" << i+1 << ": " << v[i] << endl;
		out_file.close();
	}
}

int main()
{
    vector<int> results;

    readInput("C-small.in", results);
    writeOutput("C-small.out", results);
    return 0;
}

