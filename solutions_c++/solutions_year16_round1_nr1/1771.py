#include <fstream>
#include <cstring>
#include <string>

using namespace std;

int main(){
	ifstream fin ("A-large.in");
	ofstream fout ("A-output.txt");
	int t;
	fin >> t;
	char input[1001];
	string output;
	for (int i = 1; i <= t; i++){
		fin >> input;
		output = "";
		for (int x = 0; x < strlen(input); x++){
			if (output[0]<=input[x]){
				output = input[x] + output;
			} else {
				output = output + input[x];
			}
		}
		fout << "Case #" << i << ": " << output << '\n';
	}
	return 0;
}
