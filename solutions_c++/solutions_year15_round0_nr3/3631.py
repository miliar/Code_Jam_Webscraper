#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>
#include <cmath>
#include <unordered_set>

using namespace std;

int table[4][4] = {{1, 2, 3, 4},
				   {2,-1, 4,-3},
				   {3,-4,-1, 2},
				   {4, 3,-2,-1}};


bool search_ijk(string &str, long X) {
	unordered_set<long> set_j;
	unordered_set<long> set_k;
	int val = 1, pos;

	long total_size = str.size() * X;

	pos = str.size()-1;
	for (long i = total_size-1; i >= 0; i--) {
		int curr = str.at(pos) - 'g';
		if(signbit(val))
			val = table[curr-1][abs(val)-1] * (-1);
		else
			val = table[curr-1][abs(val)-1];

		if (val == 4) {
			set_k.insert(i);
		}
		pos--;
		if (pos == -1)
			pos = str.size()-1;
	}

	for (long i = 0; i < total_size; i++) {
		val = 1;
		pos = i%str.size();
		for (long j = i; j < total_size; j++) {
			int curr = str.at(pos) - 'g';
			if(signbit(val))
				val = table[abs(val)-1][curr-1] * (-1);
			else
				val = table[abs(val)-1][curr-1];

			if (val == 3 && (set_k.find(j+1) != set_k.end())) {
				set_j.insert(i);
				break;
			}
			pos++;
			if (pos == str.size())
				pos = 0;
		}
	}

	val = 1;
	pos = 0;
	for (long i = 0; i < total_size; i++) {
		int curr = str.at(pos) - 'g';
		if(signbit(val))
			val = table[abs(val)-1][curr-1] * (-1);
		else
			val = table[abs(val)-1][curr-1];

		if (val == 2 && (set_j.find(i+1) != set_j.end())) {
			return true;
		}

		pos++;
		if (pos == str.size())
			pos = 0;
	}

	return false;
}

int main() {
    int numCases;
    
    ifstream infile("C-small-attempt1.in");
    infile >> numCases;
    int count = 0;

    while (count < numCases) {
		int L;
		long X;
		string str;
		bool result;

		infile >> L;
		infile >> X;
		infile >> str;

		if (str.size() != L) {
			cout << "Error: Bad input!" << endl;
			exit(0);
		}
		result = search_ijk(str, X);

        count++;
        cout << "Case #" << count << ": " << (result == true ? "YES" : "NO") << endl;
    }
 
    return 0;
}
