#include <iostream>
#include <fstream>
#include <string>

using namespace std;
bool DEBUGFLAG=false;

int process(string input){
	int result=0;
	for (int i = 0; i < input.size()-1; ++i)
		if (input[i] != input[i+1]) ++result;
	if (input.back() == '-') ++result;
	return result;
}

int main(int argc, char **argv){
	string filename;
	for (int i = 1; i < argc; ++i)
		if (string("--debug").compare(argv[i])==0) DEBUGFLAG=true;
		else filename = string(argv[i]);
	ifstream ip(argv[1]);
	ofstream op("output.txt");
	int N;
	string input;
	ip >> N;
	for (int i =0 ; i < N; ++i){
		ip>>input;
		op << "Case #" << i+1 << ": " << process(input) << endl;
	}
	op.close();
	ip.close();
	return 0;
}