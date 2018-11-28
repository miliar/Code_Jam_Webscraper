#include <iostream>
#include <fstream>

using namespace std;
int main() 
{	int a1, a2;
	int t1[4][4], t2[4][4];
	int fl[16];
	
	ifstream f1;
	f1.open("in.txt");
	
	ofstream f2;
	f2.open ("out.txt");
	
	int nt;
	f1 >> nt;

	
	for (int t=0; t<nt; t++)
	{
		for (int i=0; i<16; i++)
			fl[i]=0;

		f1 >> a1;

		for (int i=0; i<4; i++)
		for (int j=0; j<4; j++)
			f1>>t1[i][j];

		for (int j=0; j<4; j++)
			fl[t1[a1-1][j]-1]++;
		
		f1 >> a2;

		for (int i=0; i<4; i++)
		for (int j=0; j<4; j++)
			f1>>t2[i][j];
		
		for (int j=0; j<4; j++)
			fl[t2[a2-1][j]-1]++;
		

		int c=0;
		int r=-1;
		for (int i=0; i<16; i++)
			if (fl[i]==2)
			{ c++; r=i+1;}

		if (c==0)
			{f2 <<"Case #"<< t+1 <<": Volunteer cheated!\n";}
			else
			{ if (c==1)
				{f2 <<"Case #"<< t+1 <<": " << r <<"\n";}
				else
				{f2 <<"Case #"<< t+1 <<": Bad magician!\n";}
			}
			
	}
	
	f1.close();
	f2.close();
    return 0; 
}