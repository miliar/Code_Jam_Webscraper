#include <fstream>
#include <iostream>

using namespace std;

int main(int argc, char* argv[])
{
	int cases=0;
	int a,b,aLoc,bLoc;
	a=b=aLoc=bLoc=0;
	if(argc!=3)
	{
		cerr<<"improper command, FairandSquare inputfile outputfile\n";
		return 1;
	}
	ifstream inFile(argv[1], ios_base::in);
	ofstream outFile(argv[2], ios_base::out);
	if(!inFile)
	{
		cerr<<"input file not found\n";
		return 2;
	}
	//quick and dirty palindrome squares under 1000
	int palinSquareArray[]={1,4,9,121,484};
	inFile>>cases;
	for(int i=0;i<cases;++i)//outer loop, cases
	{
		aLoc=0;bLoc=4;
		inFile>>a;
		inFile>>b;
		for(int j=0;j<5;++j)
		{
			if(a>palinSquareArray[j])
				aLoc=j+1;
			if(b<palinSquareArray[4-j])
				bLoc=4-j-1;
		}
		outFile<<"Case #"<<i+1<<": ";
		if(aLoc>bLoc)
		{
			outFile<<"0\n";
		}
		else
		{
			outFile<<bLoc-aLoc+1<<'\n';
		}
	}//end outer loop: cases
	//closing files
	inFile.close();
	outFile.close();
	return 0;

}