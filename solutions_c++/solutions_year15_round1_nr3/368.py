#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

ifstream fin("3.in");
ofstream fout("3.out");

long long int x[10000],y[10000];
int answer[10000];

int main(){
	int nCases;
	fin >> nCases;
	for(int t=1;t<=nCases;t++){
		int n;
		fin >> n;
		for(int i=0;i<n;i++){
			fin >> x[i] >> y[i];
			answer[i] = 10000;
		}

		if(n==1)
			answer[0] = 0;
		
		for(int t1=0;t1<n;t1++){
			for(int t2=0;t2<t1;t2++){
				int posCount = 0;
				int negCount = 0;
				long long int vx = x[t2]-x[t1];
				long long int vy = y[t2]-y[t1];
				long long int val = vx*y[t1] - vy*x[t1];
				for(int t3=0;t3<n;t3++){
					long long int result = vx*y[t3] - vy*x[t3];
					if(result < val)
						negCount++;
					if(result > val)
						posCount++;
				}
				answer[t1] = min(answer[t1],negCount);
				answer[t1] = min(answer[t1],posCount);
				answer[t2] = min(answer[t2],negCount);
				answer[t2] = min(answer[t2],posCount);
			}
		}
		
		fout << "Case #" << t << ":" << endl;
		for(int i=0;i<n;i++){
			fout << answer[i] << endl;
		}
	}
	return 0;
}