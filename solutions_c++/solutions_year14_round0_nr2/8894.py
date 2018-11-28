#include <iostream>
#include <cstdio>
#include <fstream>
#include <iomanip>
using namespace std;

int main() {
    ifstream fin;
    ofstream fout;
    fin.open("B-large.in");
    fout.open("output.txt");
	int t;
	fin>>t;
	int ff=1;
	while(t--) {
		fout<<"Case #"<<ff<<": ";
		ff++;
		double c,f,x;
		fin>>c>>f>>x;
		double bestAnswer = x/2.0;
		int k=1;
		while(1) {
			double answer = 0.0,rate=2.0;
			for(int i=0;i<k;i++) {
				answer+=c/rate;
				rate+=f;
			}
			answer+=x/rate;
			if(answer>bestAnswer)
				break;
			bestAnswer = answer;
			k++;
		}
		fout<<setprecision(10)<<bestAnswer<<endl;
	}
	return 0;
}
