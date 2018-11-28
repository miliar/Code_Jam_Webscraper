#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

ifstream fin("d.in");
ofstream fout("d.out");

long long intpow(int x, int n) {
	long long y = 1;
	for(int i=0; i<n; i++)
		y *= x;
	return y;
}

void printsmall(int K, int C) {
	long long step = intpow(K,C-1);
	long long tile = 0L;
	for(int i=0; i<K; i++) {
		fout << (tile+1) << " ";
		tile += step;
	}
}

void printtiles(int K, int C, int S) {
	if(K==S) {
		printsmall(K,C);
	}
}


int main() {

	int T; fin>>T;
	for(int t=1; t<=T; t++) {
		int K,C,S;
		fin >> K >> C >> S;
		fout << "Case #" << t << ": ";
		printtiles(K,C,S);
		fout << endl;
	}

	return 0;
}

