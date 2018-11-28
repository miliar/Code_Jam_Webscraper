/*input
*/
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>


using namespace std;

char S[101];

bool testStack(){
	bool ret = true;
	int i = 0;
	while(S[i] != '\0'){
		if(S[i] == '-'){
			ret = false;
		}
		i++;
	}
	return ret;
}

void flip(int n){
	for(int i = 0; i < n && S[i] != 0; i++){
		if(S[i] == '-')
			S[i] = '+';
		else
			S[i] = '-';
	}
}

int stackSize(){
	int size = 0;
	for(int i = 0; i < 101; i++){
		if(S[i] == '\0')
			break;
		size++;
	}
	return size;
}

int main(){
    ofstream fout ("B-large.out");
    ifstream fin ("B-large.in");

	int T;
	fin >> T;

	for(int t = 0; t < T; t++){
		fout << "Case #" << t+1 << ": ";
		fin >> S;

		int size = stackSize();
		int flips = 0;

		while(!testStack()){

			for(int i = size - 1; i >= 0; i--){
				if(S[i] == '-'){
					flip(i+1);
					break;
				}
			}
			flips++;
		}
		fout << flips << endl;
	}

	return 0;
}