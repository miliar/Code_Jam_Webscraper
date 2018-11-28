// ConsoleApplication20.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in;
	in.open("A-small-attempt0 (1).in");
	ofstream out;
	out.open("output.txt");
	int test=0;
	in>>test;
	int f_input=0;
	int s_input=0;

	int array1[4][4];
	int array2[4][4];
	
	for(int i=0;i<test;i++)
	{
		in>>f_input;
		cout<<f_input<<endl;
		f_input--;
		
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				
				in>>array1[j][k];
				//cout<<array1[j][k]<<" ";

			}
			//cout<<endl;
		}


		in>>s_input;
		cout<<s_input<<endl;
		s_input--;
		
		//cout<<endl;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				
				in>>array2[j][k];
				//cout<<array2[j][k]<<" ";

			}
			//cout<<endl;
		}


		//check portion

		int value=-1;
		int count=0;
		for(int y=0;y<4;y++)
		{
			for(int z=0;z<4;z++)
			{
				if(array1[f_input][y]==array2[s_input][z])
				{
					value=array1[f_input][y];
					
					count++;
				}
			}

		}
		if(value==-1)
		{
			out<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;

		}
		else if(count==1)
		{
					out<<"Case #"<<i+1<<": "<<value<<endl;
		}
		else if(count>1)
		{
			out<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
		}


	}


	return 0;
}

