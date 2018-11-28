#include<iostream>
#include<fstream>
#include <cstring>

using namespace std;

int main() {
	ifstream fin;
	ofstream fout;
	
	fin.open("B-large.in");
	fout.open("output.out");
	
	int t;
	char s[200];
	
	fin>>t;
	fin.getline(s, 200);
	for (int testcase=0; testcase<t; testcase++) {
		fin.getline(s, 200);
		
		// All '-'
		int f = 0;
		for (int i=0; i< strlen(s); i++) {
			if (s[i]!='-') {
				f = 1;
				break;
			}
		}
		if (f==0) {
			fout<<"Case #"<<(testcase+1)<<": "<<"1"<<"\n";
			continue;
		}
		
		// All '+'
		f = 0;
		for (int i=0; i< strlen(s); i++) {
			if (s[i]!='+') {
				f = 1;
				break;
			}
		}
		if (f==0) {
			fout<<"Case #"<<(testcase+1)<<": "<<"0"<<"\n";
			continue;
		}
		
		//Find number of '-' groups
		int nGroups = 0, inNGroup = 0;
		for (int i=0; i< strlen(s); i++) {
			if (s[i]=='-') {
				if (!inNGroup) {
					nGroups++;
				}
				inNGroup=1;
			} else {
				inNGroup=0;
			}
		}
		if (s[0]=='+')
			fout<<"Case #"<<(testcase+1)<<": "<<nGroups*2<<"\n";
		else
			fout<<"Case #"<<(testcase+1)<<": "<<((nGroups-1)*2)+1<<"\n";
		
	}
	
	
	return 0;
}
