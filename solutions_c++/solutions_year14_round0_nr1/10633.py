#include <iostream>
#include <conio.h>
#include <fstream>

using namespace std;

int main() {
	int tests;
	ifstream fin;
	fin.open("A-small-attempt0.in");
	ofstream fout;
	fout.open("output.txt");
	fin>>tests;
	for (int totCount = 0; totCount<tests; totCount++ ) {
		int ans1, ans2;
		fin>>ans1;
		
		int set1[4], set2[4], dumdum;
		
		for(int i=0; i<4; i++) {
			for(int j =0; j<4; j++) {
				if(i==ans1-1) { fin>>set1[j]; }
				else fin>>dumdum;
			}
		}
		
		//cout<<"\n";
		
		fin>>ans2;
		
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				if(i==ans2-1) { fin>>set2[j]; }
				else fin>>dumdum;
			}
		}
		
		//cout<<"\n";
		
		int count=0; int val = 0;
		
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				if(set1[i] == set2[j]) { count++; val=set1[i]; }
				if (count>1) { j=50; i=50; }
			}
		}
		
		fout<<"Case #"<<totCount+1<<": ";
		
		if(count==0) fout<<"Volunteer cheated!";
		else if(count==1) fout<<val;
		else fout<<"Bad magician!";
		
		if(totCount!=tests-1) {fout<<"\n";}
	}
	return 0;
}
