#include <iostream>
#include <fstream>
using namespace std;

int numberToAdd(int A[], int l);

int main()
{
	int T,Smax;
	char c;
	ifstream read;
	ofstream write;
	read.open("A-large.txt");
	write.open("outputProbAsmall.txt");
	
	read>> T;
	
	for (int i=0; i<T; i++)
	{
		read>> Smax;
		int *A = new int [Smax];
		for (int j=0; j<=Smax; j++)
		{
			read>> c;
			A[j] = c - '0';
		}
		write <<"Case #"<<i+1<<": "<<numberToAdd(A,Smax)<<endl;
	}
}

int numberToAdd(int A[], int l)
{
	int nClap = A[0];
	int nToAdd = 0;
	int nToAddTemp;
	for(int i=1; i<=l; i++)
	{
		if(nClap >= i)
			nClap = nClap + A[i];
		else 
		{
			nToAddTemp = i - nClap;
			nClap = nClap + nToAddTemp + A[i];
			nToAdd = nToAdd + nToAddTemp;
		}
	}
	return nToAdd;
}