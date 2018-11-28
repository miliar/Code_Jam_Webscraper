#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main() {
	ofstream fout;
	ifstream fin;

	fin.open("a.in");
	fout.open("a.out");

	int T;
	string buf;
    
	fin >> T;
    
	for (int i = 0; i != T; i++) {
		long n, left, ret = 0;
		fin >> buf;
		fin >> n;
        
		left = 0;
		long con = 0;
        
		for (long j = 0; j != buf.size(); j++) {
			left++;
			if (buf[j] == 'a' || buf[j] == 'e' || buf[j] == 'i' || buf[j] == 'o' || buf[j] == 'u') {
                con = 0;
			}
			else {
				con++;
				if (con == n) {
					ret += (left - n + 1) * (buf.size() - j);
					left = --con;
				}
			}
		}
        
		fout << "Case #" << i + 1 << ": " << ret << endl;
	}
    
	return 0;
}
