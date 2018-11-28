#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#define INPUTFILE "input.in"
#define OUTPUTFILE "output.out"

void compute(int index, std::ifstream & inp, std::ofstream & out){
	int sm;
	inp >> sm;
	std::string sstr;
	inp >> sstr;
	int cnt = 0;
	int num = 0;
	for(int s = 0; s <= sm; s++){
		int c = sstr[s] - '0';
		if(cnt < s){
			int diff = s - cnt;
			num += diff;
			cnt += diff;
		}
		cnt += c;
	}
	out << "Case #" << index + 1 << ": " << num << std::endl;
}

void main(){
	std::string sT;
	std::ifstream infile(INPUTFILE);
	std::ofstream outfile(OUTPUTFILE);
	if(infile.is_open() && outfile.is_open()){
		int T;
		infile >> T;
		for(int t = 0; t < T; t++){
			compute(t, infile, outfile);
		}
	}
	if(infile.is_open())
		infile.close();
	if(outfile.is_open())
		outfile.close();
}