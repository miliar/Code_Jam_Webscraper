#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <sstream>
#include <string>
#include <array>

using namespace std;

int length(int N) {
	int length = 0;
	while (N > 0) {
		length++;
		N /= 10;
	}
	return length;
}

int des(int n) {
	int des = 1;
	if (n > 0)
		for (int i = 1; i <= n; i++) {
			des *= 10;
		}
	return des;
}

int invert(int num) {
	int res = 0;
	while (num > 0)
	{
		res = res * 10 + (num % 10);
		num = num / 10;
	}
	return res;
}

bool check(array<bool, 10>& n) {
	for each (bool b in n) {
		if (b == false)
			return false;
	}
	return true;
}

int main()
{
	ifstream in("B-large.in");
	//ifstream in("A-large.in");
	ofstream out("outlarge.out");
	
	/*unsigned long*/ long int T;
	string line, result;
	if (in.is_open()){
		in >> T;
		
		for (int i = 1; i <= T; i++){
			in >> line;
			char last = line[0];
			int count = 0;
			int changes = 0;
			for each (char c in line) {
				if (c != last) {
					last = c;
					changes++;
				}
				count++;
			}
			if (line[0] == '-' && changes % 2 == 0)
					changes++;
			if (line[0] == '+' && changes % 2 == 1)
				changes++;
			out << "Case #" << i << ": " << changes << endl;
		}
		in.close();
	}
	out.close();
	return 0;
}