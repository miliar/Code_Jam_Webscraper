#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;

struct D { 
	double P; // 생산성 (i개의 farm을 가질 때의 생산성)
	double T; // i개의 farm을 가질 때까지 걸리는 최소 시간
	double TargetTime;
};

int main() {
	int N, MaxFarmCNT;
	double C, F, X;
	ifstream fin;
	ofstream fout;
	
	fin.open("B-large.in");
	fout.open("B-large-answer.in");
	fin >> N;
	D *Farm;
	for(int mcase=1;mcase<=N;mcase++) {
		fin >> C >> F >> X;
		MaxFarmCNT = (X/C)+1;
		Farm = new D[MaxFarmCNT+1];
		Farm[0].P = 2;
		Farm[0].T = 0;
		Farm[0].TargetTime = (X/2);
		fout << "Case #";
		fout << mcase << ": ";
		for(int i=1;i<=MaxFarmCNT;i++) {
			Farm[i].T = Farm[i-1].T + (C/Farm[i-1].P);
			Farm[i].P = Farm[i-1].P + F;
			Farm[i].TargetTime = ((X/Farm[i].P)+Farm[i].T);
			if(Farm[i].TargetTime > Farm[i-1].TargetTime) {
				fout.precision(log10(Farm[i-1].TargetTime)+8);
				fout << Farm[i-1].TargetTime << endl;
				break;
			}
		}
	}
	fout.close();
	return 0;
}