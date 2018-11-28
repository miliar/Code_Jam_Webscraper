#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;


void main()
{
	fstream file;
	file.open("A-small-attempt2.in");


	char in[10];
	
	file>>in;
	int cases=atoi(in);

	char input1[10],input2[10];


	int array[4][4];
	int array2[4][4];

		fstream file2;
		file2.open("output.txt");

	for(int i=0;i<cases;i++)
	{
		file>>input1;
		int in1=atoi(input1);
		in1--;
		for(int l=0;l<4;l++)
		{
			for(int j=0;j<4;j++)
			{
				file>>in;
				int temp=atoi(in);
				array[l][j]=temp;
			}
		}


		file>>input2;
		int in2=atoi(input2);
		in2--;
		for(int l=0;l<4;l++)
		{
			for(int j=0;j<4;j++)
			{
				file>>in;
				int temp=atoi(in);
				array2[l][j]=temp;
			}
		}


		int num=0;int count=0;

		for(int a=0;a<4;a++)
		{
			for(int b=0;b<4;b++)
			{
				if(array[in1][a]==array2[in2][b])
				{
					count++;
					num=array[in1][a];
				}

			}
		}

		if(count==0)
		{
			file2<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		}
		else if(count>1)
		{
			file2<<"Case #"<<i+1<<": Bad magician!"<<endl;
		}
		else
		{
			file2<<"Case #"<<i+1<<": "<<num<<endl;
		}
		
		
	}


file2.close();


	file.close();
}