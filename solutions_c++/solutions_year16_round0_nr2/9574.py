#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int find_answer(string s_passin){
	string s = s_passin;
	char c = '-';
	int total = 0;
	//cout << s.find_last_of("-") << endl;
	while(s.find_last_of(c) != -1){
		s = s.substr(0, s.find_last_of(c));
		total++;
		if (c == '-'){
			c = '+';
		}
		else{
			c = '-';
		}
	}
	//cout << s.substr(0, s.find_last_of("-")) << endl;
	return total;
}

int main(int argc, char *argv[]) {
	int n;
	ifstream infile("B-large.in");
	//infile.open();
	ofstream outfile("outputp2.txt");
	//outfile.open();
	
	infile >> n;
	//cout << n;
	for (int i = 0; i < n; i++){
		string s;
		infile >> s;
		outfile << "Case #"<< i+1 << ": "<< find_answer(s) << endl;
	}	
	
	infile.close();
	outfile.close();

}