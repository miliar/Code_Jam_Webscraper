#include <stdio.h>
#include <fstream>

using namespace std;

ifstream fin("1.in");
ofstream fout("1.out");

int main(){
	int nCases;
	fin >> nCases;
	for(int t=1;t<=nCases;t++){
		int n;
		fin >> n;
		n++;

		char c;
		int accum = 0;
		int worst = 0;
		for(int i=1;i<=n;i++){
			fin >> c;
			accum += c - '0';
			worst = min(worst, accum-i);
		}

		fout << "Case #" << t << ": " << -worst << endl;
	}
	return 0;
}