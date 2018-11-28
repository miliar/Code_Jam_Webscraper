#include<iostream>
#include<fstream>

using namespace std;

int main() {
	ifstream fin;
	ofstream fout;
	
	fin.open("A-large.in");
	fout.open("output.out");
	
	int t, n, tp, ta, c, tempa;
	char c1;
	
	fin>>t;
	for (int testcase=0; testcase<t; testcase++) {
		fin>>n;
		tp = 0;
		ta = 0;
		for (int i=0;i<=n;i++) {
			fin>>c1;
			c = (int)c1-48;
			if (i==0 && c==0) {
				ta++;
				tp++;
			} else {
				if (i==0) {
					tp = c;
				} else {
					if (tp>=i) {
						tp += c;
					} else {
						tempa = i-tp;
						ta += tempa;
						tp += tempa+c;
					}
				}
			}
		}
		fout<<"Case #"<<(testcase+1)<<": "<<ta<<"\n";
	}
	
	
	return 0;
}
