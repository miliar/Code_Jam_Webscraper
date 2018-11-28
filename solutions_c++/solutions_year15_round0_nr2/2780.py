#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#define INPUTFILE "input.in"
#define OUTPUTFILE "output.out"

int getCount(std::vector<int> & arr, int N){
	unsigned len = arr.size();
	int cnt = 0;
	for(unsigned i = 0; i < len; i++){
		cnt += ((arr[i]-1)/N);
	}
	cnt += N;
	return cnt;
}

void compute(int index, std::ifstream & inp, std::ofstream & out){
	int D;
	inp >> D;
	std::vector<int> arr;
	arr.reserve(D);
	int max = 0;
	for(int i = 0; i < D; i++){
		int p;
		inp >> p;
		arr.push_back(p);
		if (max < p) max = p;
	}
	int cur = max;
	int curCnt = max;
	for(int i = max-1; i > 0; i--){
		int val = getCount(arr, i);
		if(val < cur) cur = val;
	}
	out << "Case #" << index + 1 << ": " << cur << std::endl;
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