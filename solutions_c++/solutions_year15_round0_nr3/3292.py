#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <ctime>

using namespace std;

int quaternion[4][4] = { { 1, 2, 3, 4 }, { 2, -1, 4, -3 }, { 3, -4, -1, 2 }, { 4, 3, -2, -1 } };
bool findI(long start, long end, long *charSeq);
bool findJ(long start, long end, long *charSeq);
bool findK(long start, long end, long *charSeq);

int main(){

	string info;
	ifstream problemFile;
	problemFile.open("C-small-attempt2.in");
	ofstream problemSolution;
	problemSolution.open("problemC_small.txt");
	getline(problemFile, info);
	int testCases = atoi(info.c_str());

	for (int i = 0; i < testCases; i++){
		string status = "NO";
		int currChar = 0;
		int chars = 0;
		long repeat = 0;

		getline(problemFile, info);
		istringstream nums(info);
		nums >> chars >> repeat;

		long *charSeq = (long*)malloc(sizeof(long) * chars*repeat);

		getline(problemFile, info);
		string str = info;
		if (chars * repeat > 2){
			for (long j = 0; j < repeat; j++){
				long k = 0;
				for (char c : str){
					int tmpChar;
					if (c == 'i'){
						tmpChar = 2;
					}
					if (c == 'j'){
						tmpChar = 3;
					}
					if (c == 'k'){
						tmpChar = 4;
					}
					charSeq[((chars * j) + k)] = tmpChar;
					k++;
				}
			}
			if (findI(0, (chars * repeat), charSeq)){
				status =  "YES";
			}
		}
		problemSolution <<  "Case #" << (i+1) << ": " << status << "\n";
	}
	problemFile.close(); problemSolution.close();
}

/*
i = 2, j = 3, k = 4.
*/
bool findI(long start, long end, long *charSeq){
	int tmpChar = 0;
	for (long i = start; i < end; i++){
		if (tmpChar == 0 ){
			tmpChar = charSeq[i];
		}
		else{
			if (tmpChar < 0){
				tmpChar = (-1)*quaternion[((-1)*tmpChar) - 1][charSeq[i] - 1];
			}
			else{
				tmpChar = quaternion[tmpChar - 1][charSeq[i] - 1];
			}
		}
		if (tmpChar == 2){
			if (findJ(i + 1, end, charSeq)){
				return true;
			}
		}
	}
	return false;
}
/*
i = 2, j = 3, k = 4.
*/
bool findJ(long start, long end, long *charSeq){
	int tmpChar = 0;
	for (long i = start; i < end; i++){
		if (tmpChar == 0){
			tmpChar = charSeq[i];
		}
		else{
			if (tmpChar < 0){
				tmpChar = (-1)*quaternion[(-1)*tmpChar - 1][charSeq[i] - 1];
			}
			else{
				tmpChar = quaternion[tmpChar - 1][charSeq[i] - 1];
			}
		}
		if (tmpChar == 3){
			if (findK(i + 1, end, charSeq)){
				return true;
			}
		}
	}
	return false;
}
/*
i = 2, j = 3, k = 4.
*/
bool findK(long start, long end, long *charSeq){
	int tmpChar = 0;
	for (long i = start; i < end; i++){
		if (tmpChar == 0){
			tmpChar = charSeq[i];
		}
		else{
			if (tmpChar < 0){
				tmpChar = (-1)*quaternion[(-1)*tmpChar - 1][charSeq[i] - 1];
			}
			else{
				tmpChar = quaternion[tmpChar - 1][charSeq[i] - 1];
			}
		}
		if (tmpChar == 4){
			if (i == (end - 1)){
				return true;
			}
		}
	}
	return false;
}