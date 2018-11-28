#include <iostream>
#include <fstream>
using namespace std;

int main() 
{
	ofstream myfile;
  	myfile.open ("test.out");	
	ifstream infile;
	infile.open("A-small-attempt1.in");
	int testCase;
	infile>>testCase;
	for(int i=1;i<testCase+1;++i) {
		int result = 0;
		int num;
		int firstRow, secondRow;
		int temp;
		int numF[4];
		infile>>firstRow;
		for(int j=0;j<16;++j) {
			infile>>temp;
			if(j/4==firstRow-1) {
				numF[j%4] = temp;			
			}
		}
		infile>>secondRow;
		for(int j=0;j<16;++j) {
			infile>>temp;
			if(j/4==secondRow-1) {
				for(int k=0;k<4;++k)
					if(temp==numF[k])
					{num = temp;	++result;}			
			}
		}
		if(result==0)
			myfile<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		else if(result==1)
			myfile<<"Case #"<<i<<": "<<num<<endl;
		else
			myfile<<"Case #"<<i<<": Bad magician!"<<endl;
	}
}
