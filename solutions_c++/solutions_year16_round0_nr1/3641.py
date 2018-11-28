#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int T;
long long N;
bool digits[10];
bool advancee = false;


int main() {
	ifstream fin;
	fin.open("A-large.in");
	freopen("A-large.out", "w", stdout);
	fin >> T;

	for(int i = 0; i < T; i++) {
		fin >> N;
		for(int j = 0; j < 10; j++) digits[j] = false;
		if(N != 0) {
			for(int j = 1; !advancee; j++) {
				stringstream ss;
				ss << (j*N);
				string temp = ss.str();
				for(int k = 0; k < (int)temp.length(); k++) {
					if(!digits[temp.at(k) - '0']) digits[temp.at(k) - '0'] = true;
				}
				int t;
				for(t = 0; t < 10 && digits[t]; t++);
				if(t == 10) {
					cout << "Case #" << i+1 << ": " << temp << endl;
					advancee = true;
				}
				//cout << " " << temp << endl;
				//temp = "";
			}
			advancee = false;
		}
		else cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
	}


	return 0;
}