#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

ifstream fin("1.in");
ofstream fout("1.out");

int m[5000];

int main(){
	int nCases;
	fin >> nCases;
	for(int t=1;t<=nCases;t++){
		int n;
		fin >> n;
		for(int i=0;i<n;i++){
			fin >> m[i];
		}
		
		int answer1 = 0;
		int maxPer = 0;
		for(int i=1;i<n;i++){
			answer1 += max(0,m[i-1] - m[i]);
			if(m[i-1]-m[i] > maxPer){
				maxPer = m[i-1] - m[i];
			}
		}
		int answer2 = 0;
		for(int i=0;i<n-1;i++){
			answer2 += min(maxPer, m[i]);
		}

		fout << "Case #" << t << ": " << answer1 << " " << answer2 << endl;
	}
	return 0;
}