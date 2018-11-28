#include<iostream>
#include<fstream>
#include<conio.h>
using namespace std;

void main()
{
	int testCases; int A1,A2,C1,C2;
	int A1Rows[16]; int F1Row[4]; int Num;
	int A2Rows[16];int F2Row[4]; int Res;
	ifstream infile; ofstream ofile;
	ofile.open("A_Small.txt");
	infile.open("A-small-attempt0.in");
	infile>>testCases;
	for(int i=0;i<testCases;i++)
	{
		Res=0;
		infile>>A1;
		C1=4*(A1-1);
		for(int j=0;j<16;j++)
		infile>>A1Rows[j];
		infile>>A2;
		C2=4*(A2-1);
		for(int j=0;j<16;j++)
		infile>>A2Rows[j];
		for(int k=0;k<4;k++)
		{	
			F1Row[k]=A1Rows[C1];
			C1++;
		}
		for(int k=0;k<4;k++)
		{	
			F2Row[k]=A2Rows[C2];
			C2++;
		}

		for(int q=0;q<4;q++)
			for(int w=0;w<4;w++)
				if(F1Row[q]==F2Row[w])
				{
					Res++;
					Num=F1Row[q];
				}
		if(Res==1)
			ofile<<"Case #"<<i+1<<": "<<Num<<endl;
		else if(Res==0)
			ofile<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		else if(Res>1)
			ofile<<"Case #"<<i+1<<": Bad magician!"<<endl;
		
	}
	infile.close();
	ofile.close();
}