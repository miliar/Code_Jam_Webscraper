#include <iostream>
#include <fstream>

using namespace std;
void update(int* A,int count) {
	while(count)
	{
	int index= count%10;
	A[index]=1;
	count=count/10;
}
}
int main() {
	ifstream infile;
	infile.open("input.txt");
	ofstream outfile;
	outfile.open("output.txt");
	unsigned long int N;
	unsigned int T;
	infile>>T;
	int A[10];
	for(int i=1; i<=T; i++) {
		infile>>N;
		if(N<0) return -1;
		if(N==0) 
		{
			outfile<<"Case #"<<i<<": INSOMNIA"<<endl;
		}
		else
		{ for(int m=0;m<=9;m++) A[m]=0;
		unsigned long int count=0;
		int checksum;
		
		do{ checksum=1;
			count +=N;
			update(A,count);
			for(int j=0;j<=9 ;j++ ) {
			checksum= checksum*A[j]; 
			if(!checksum) break;
		}
	}
		while(!checksum);
		outfile<<"Case #"<<i<<": "<<count<<endl;
	 }
 }
}
