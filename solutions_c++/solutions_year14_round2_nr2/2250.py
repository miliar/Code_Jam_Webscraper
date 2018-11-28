#include <cstdlib>
#include <iostream>
#include <string.h>
#include <vector>
#include <stdio.h>
#include <fstream>
using namespace std;

ofstream myAns;
ifstream Qfile;

void Solve(int CaseNum)
{
	int A,B,K;
	int pairs=0;
	 
	Qfile>>A;
	Qfile>>B;
	Qfile>>K;

	for(int a=0;a<A;a++)
	{
		for(int b=0;b<B;b++)
		{
			for(int k=0;k<K;k++)
			{
				if((a&b)==k) pairs++;
			}
		}
	}


	myAns<<"Case #"<<CaseNum<<": ";
	myAns.precision(15);
	myAns<<pairs;
	myAns<<endl;
}

int main(int argc, char *argv[])
{
	int T=0;
	int i=0;

	Qfile.open("B-small-attempt0.in");
	myAns.open ("MyAnser.txt");
		
	Qfile>>T;	
	
	for(i=0; i<T; i++)	
	{						
		Solve(i+1);
	}
	myAns.close();
	Qfile.close();
    
	system("PAUSE");
    return EXIT_SUCCESS;
}
