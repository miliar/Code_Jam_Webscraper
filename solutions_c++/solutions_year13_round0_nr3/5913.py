#include <iostream>
#include <math.h>
#include <cmath>
#include <fstream>




using namespace std;

char board[4][4];

int main()

{

	ifstream fin("input.in");
	ofstream fout("output.in");

	int T;

	long int a[39]= {1,2,3,11,22,101,111,121,202,212,1001,1111,2002,11211,10001,10101,10201,11011,11111,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,2000002,2001002,1111111};

	fin >> T; 

	int t= 1;
	while(T--)
	{

		double A, B;
		int countA, countB;
		fin >>A >>B;

		A = sqrt((double)A);
		B = sqrt((double)B);

		
		for(int i=0; i< 39; i++)
		{
			
			if(a[i]>=A)
			{
				countA=i;
				break;
			}
		}
		
			
		for(int i=0; i< 39; i++)
		{
			if(a[i]==B)
			{	countB = i+1;
				break;
			}
			if(a[i]>B)
			{
				countB=i;
				break;
			}
		}
		

		fout <<"Case #"<<t<<": "<< countB-countA << endl;


	t++;
	}

	fin.close();
	fout.close();

}

