/*
GOOGLE JAM CODE:
ES 1, MAGIA
*/

#include <fstream>
#include <iostream>
#include <stdio.h>

using namespace std;
int casi;


int main ()
{
	ifstream in ("input.txt");
	int T; //number of  cases
	in>>T;
	
	ofstream out("ouput.txt");
	
	for (casi=1; casi<=T; casi++)
	{
		//input
		int riga;
		int uguale;
		
		int vettore1[4], vettore2[4];
		
		in>>riga;
		
		for (int j=0; j<4; j++)
			for(int i=0; i<4; i++)
			{
				if (j==riga-1)
					in>>vettore1[i];
				else in>>uguale;
			}
		
		in>>riga;
		
		for (int j=0; j<4; j++)
			for(int i=0; i<4; i++)
			{
				if (j==riga-1)
					in>>vettore2[i];
				else in>>uguale;
			}
			
		
		uguale=0;
		for (int j=0; j<4; j++)
			for(int i=0; i<4; i++)
			{
				if (vettore1[j]==vettore2[i])
				{
					uguale++;
					riga=vettore1[j];
				}	
			}
		
		out<<"Case #"<<casi<<": ";
		
		if (uguale==1)
			out<<riga;
		else if (uguale>1)
			out<<"Bad magician!";
		else
			out<<"Volunteer cheated!";
		
		out<<endl;
		
	}
}
