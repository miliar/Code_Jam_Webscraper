#include<fstream>
#include<iostream>
#include<string>

using namespace std;

int T;

bool isMinus(string s) {
	for(int i = 0 ; i < s.size(); i++) {
		if(s[i] =='-') {
			return true;
		}
	}
	return false;
}

int main() {
	ifstream fin("input.txt");
	if(!fin.is_open()) {
		cout<<"Error"<<endl;
	}
	ofstream fout("output.txt");
	if(!fout.is_open()) {
		cout<<"Error"<<endl;
	}
	fin>>T;
	int k = 1, result;
	string s;
	for(int i = 0 ; i < T; i++) {
		fin>>s;
		result = 0;
		while(isMinus(s)) {
			int j = 0;
			char check = s[0];
			if(check == '+' && j <s.size()) {
				while(s[j] == check) {
					s[j] = '-';
					j++;
				}
			} else {
				while(j<s.size() && s[j] == check ) {
					s[j] = '+';
					j++;
				}
			}
			result++;
		}
		fout<<"Case #"<<k++<<": "<<result<<endl;
	}
	
}