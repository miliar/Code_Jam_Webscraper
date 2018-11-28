#include <iostream>
#include <fstream>
#include <string>
#include <stack>

using namespace std;

string flip(int index, string s);
int process(string s);

int main(){
	ofstream myfile;
	myfile.open("output.txt");

	ifstream myReadFile;
	myReadFile.open("B-large.in");

	int t, m;

	string s;

	myReadFile >> t;

	for (int i = 1; i < t + 1; i++) {

		myReadFile >> s;
		m = process(s);
		
		myfile << "Case #" << i << ": " << m << endl;
		
	}
}

int process(string s){
	char c = 'c';
	int count = -1;

	for (int i = 0; i < s.length(); i++){
		if (s[i] != c){
			count++;
			c = s[i];
		}
		if (i == s.length()-1){
			if (s[i] == '-'){
				count++;
			}
		}
	}

	return count;
}

string flip(int index, string s){
	string s2 = s;
	int c = 0;

	string insert;

	for (int i = 0; i < index+1; i++){
		if (s.substr(i, 1) == "+"){
			insert = "-";
		}
		else{
			insert = "+";
		}

		s2.replace(index-i, 1, insert);
		cout << s2 << endl;
		c++;
	}

	return s2;
}