#include <cstdio> 
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

string input = "B-small-attempt0.in";
string output = "B-small-attempt0.out";


int main() {
	ifstream in(input);
	ofstream out(output);
	int t;
	in >> t;
	for (int z = 1; z <= t; z++) {
		_int64 res = 0;
		out << "Case #" << z << ": ";
		int a, b, k;
		in >> a >> b >> k;
		for (int i = 0; i < a; i++) {
			for (int j = 0; j < b; j++) {
				if ((i & j) < k)
					res++;
			}
		}
		out << res << endl;	
	}
	return 0;
}

