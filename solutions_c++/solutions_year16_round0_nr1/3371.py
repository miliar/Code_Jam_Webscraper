#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <set>
#include <iostream>

using namespace std;

set<char> digits;

void markdigits(long long x){
	ostringstream oss;
	oss << x;
	string s(oss.str());

	for(int i = 0; i < s.length(); i++)
		digits.erase(s.at(i));
}

void setdigits(string s){
	for(int i = 0; i < s.length(); i++)
		digits.insert(s.at(i));
}

int countdigits(long long x){
	ostringstream oss;
	oss << x;
	string s(oss.str());

	return s.length();
}

int main(int argc,char *argv[]){

	long long T,N;
	string s;
	ifstream fs(argv[1]);

	getline(fs, s);
	istringstream(s) >> T;
	for(int i = 0; i < T; i++){
		setdigits("0123456789");
		getline(fs,s);
		istringstream(s) >> N;
		for(long long j = 1; j < 1E+7;j++){
			markdigits(j*N);
			if (digits.empty()){
				cout << "Case #" << i+1 << ": " << j*N << endl;
				break;
			}
		}
		if (!digits.empty())
			cout << "case #" << i+1 << ": " << "INSOMNIA" << endl;
	}
}
