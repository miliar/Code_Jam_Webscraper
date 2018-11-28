

//#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <fstream>
#include <math.h>
#include <cstdio>

using namespace std;

int main()
{
	ifstream file("B-large.in");
	ofstream offile("output.txt");

	int NT = 0;

	file>>NT;


	for(int iN=0; iN<NT; iN++)
	{
		int N = 0;
		int M = 0;

		file>>N;
		file>>M;

		int** a=new int*[N]; 
		for(int i=0; i<=N;i++) 
		{ 
			a[i]=new int[M]; 
		}

		// Заполнение массива
		for(int i=0; i<N; i++)
			for(int j=0; j<M; j++)
				file>>a[i][j];

		bool Flag = true;
		for(int i=0; i<N; i++)
		{
			for(int j=0; j<M; j++)
			{
				int maxVal = a[i][j];
				bool b1 = true;
				bool b2 = true;
				for(int k=0; k<M; k++)
				{
					if(a[i][k]>maxVal)
						b1 = false;
				}
				for(int k=0; k<N; k++)
				{
					if(a[k][j]>maxVal)
						b2 = false;
				}
				if(!b1 && !b2)
					Flag = false;
			}
			
		}

		if(!Flag)
			offile<<"Case #"<<iN+1<<": NO"<<endl;
		else
			offile<<"Case #"<<iN+1<<": YES"<<endl;

 
	}

		
	return 0;
}