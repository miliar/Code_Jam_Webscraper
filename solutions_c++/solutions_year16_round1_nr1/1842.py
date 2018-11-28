#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
	// your code goes here
	int numCases;
	cin >> numCases;
	for(int i=0; i<numCases; i++){
		string strIn;
		cin >> strIn;
		string out = "";
		for(int x=0; x<strIn.length(); x++){
			string firstChar = out.substr(0, 1);
			string lastChar = out.substr(out.length(), 1);
			string compChar = strIn.substr(x, 1);
			if(compChar >= firstChar){
				out = compChar + out;
			}else if(compChar < lastChar){
				out += compChar;
			}else{
				out += compChar;
			}
		}
		cout << "Case #" << i+1 << ": " << out << "\n";
	}
	return 0;
}