#include <fstream>
#include <iostream>
#include <string>

#define THRESHOLD 100

using namespace std;

bool DEBUGFLAG=false;
typedef unsigned int numtype;

void printprocess(ostream& op, int numbering, numtype process);
numtype process (numtype input);


int main(int argc, char **argv){
	string filename;
	for (int i = 1; i < argc; ++i)
		if (string("--debug").compare(argv[i])==0) DEBUGFLAG=true;
		else filename = string(argv[i]);
	ifstream ip(argv[1]);
	ofstream op("output.txt");
	int N;
	numtype input;
	ip >> N;
	for (int i =0 ; i < N; ++i){
		ip>>input;
		printprocess(op,i,process(input));
	}
	op.close();
	ip.close();
	return 0;
}

void printprocess(ostream& op, int numbering, numtype process){
	op << "Case #" << numbering+1 << ": ";
	if (process == 0) op << "INSOMNIA";
	else op << process;
	op << endl;
	return;
}

numtype process (numtype input){
	if (input == 0) return 0;
	int check =0 ;
	numtype result=input;
	int i;
	for (i = 1; i < THRESHOLD; ++i){
		result = i*input;
		for (;result > 0; result/=10)
			check |= (1<<(result%10));
		if (check == (1<<10)-1) return i*input;
	}
	if (i == THRESHOLD) return -1;
}