#include<iostream>
#include<fstream>
using namespace std;

int main() {
	ifstream infile;
	infile.open("check.in");
	ofstream outfile;
	outfile.open("out.txt");
	int number_of_tests;
	infile>>number_of_tests;
	for(int case_number=1;case_number<=number_of_tests;case_number++) {
		int x,r,c;
		infile>>x>>r>>c;
		string answer="";
		if(r>c) {
			int temp=r;
			r=c;
			c=temp;
		}
		if(x==1)
			answer="GABRIEL";
		else if(x==2) {
			if((r==1 && c==1) ||
			  (r==1 && c==3) ||
			  (r==3 && c==3))
			  	answer="RICHARD";
			else
				answer="GABRIEL";
		}
		else if(x==3) {
			if((r==3 && c==3) ||
			  (r==2 && c==3) ||
			  (r==3 && c==4))
			  	answer="GABRIEL";
			else
				answer="RICHARD";
		}
		else if(x==4) {
			if((r==3 && c==4) ||
			  (r==4 && c==4))
				answer="GABRIEL";
			else
				answer="RICHARD";
		}
		outfile<<"Case #"<<case_number<<": "<<answer<<"\n";
	}
	return 0;
}
