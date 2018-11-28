#include <iostream>
#include <string>
using namespace std;


void flip(int hi, int * in);

int main() {
	// your code goes here
	int numCases;
	cin >> numCases;
	for(int i=0; i<numCases; i++){
		string in;
		cin >> in;
		int upSide[100];
		int length = in.length();
		for(int x=0; x<length; x++){
			if(in.substr(x,1) == "+"){
				upSide[x] = 1;
			}else{
				upSide[x] = 0;
			}
		}
		int hi = length-1;
		int lo = 0;
		bool ordered = false;
		int numFlips = 0;
		while(!ordered){
			lo = 0;
			while(upSide[hi-1] == upSide[hi])
				hi--;
			while(upSide[lo+1] == upSide[lo])
				lo++;
			if(hi <= lo){
				numFlips = (upSide[hi] == 0) ? numFlips + 1 : numFlips;
				ordered = true;
			}else{
				flip(lo, upSide);
				numFlips ++;
			}
		}
		cout << "Case #" << i+1 << ": " << numFlips << "\n";
	}
	return 0;
}

void flip(int hi, int * in){
	for(int x=0; x <= hi/2; x++){
		int temp = in[hi-x];
		in[hi-x] = 1 - in[x];
		in[x] = 1 - temp;
	}
}