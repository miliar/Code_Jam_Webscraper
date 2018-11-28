#include <iostream>
#include <string>
#include <fstream>

using namespace std;

string handle(string s){
	string result = "";
	result += s[0];
	char largest;
	largest = s[0];
	for (int i = 1; i<s.size(); i++){
		if (s[i]< largest){
			result = result + s[i];
		}
		else {
			largest = s[i];
			result = s[i] + result;
		}
	}
	return result;
}

using namespace std;
int main(int argc, char *argv[]) {
	string s;
	int n;
	ifstream infile("large1.in");
	ofstream outfile("large1.out");
	infile >> n;
	for (int i=0; i<n; i++){
		infile >> s;
		outfile << "Case #"<< i+1 << ": "<< handle(s) << endl;
	}
	infile.close();
	outfile.close();
	
}