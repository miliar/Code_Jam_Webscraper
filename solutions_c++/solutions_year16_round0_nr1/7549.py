#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string checkNum ( long long n ){
	if (n == 0 ) return "INSOMNIA";
	string s = "";
	long long i = 1;
	string number;
	while ( s.length () < 10 ) {
		number = to_string (n * i);
		for ( long long c = 0; c < number.length(); c++ ){
			if (s.find(number.substr(c,1)) == string::npos) {
    			s = s + number.substr(c,1);
    			//cout << number.substr(c,1) << endl;
			}
		}
		i++;
	}
	//cout << number << endl;
	return number;
}
int main() {
	ofstream fout ("test.out");
	ifstream fin ("A-large.in");
	int T;
	fin >> T;
	long long N;
	for ( int i = 0; i < T; i++){
		fin >> N;
		fout << "Case #" << (i+1) <<": " << checkNum(N) << endl;
	}
	return 0;
}