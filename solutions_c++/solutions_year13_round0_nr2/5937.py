// Lawnmower.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<string>
#include<fstream>
#include<sstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	string n;
	int P;
	ofstream output;
	ifstream input;
	output.open("C:/Users/mkara_000/Downloads/karara9.in");
	input.open("C:/Users/mkara_000/Downloads/B-small-attempt4.in");
	getline(input,n);
	P = stoi(n);

	bool rowsComplete = true;
	bool colsComplete = true;
	for(int t = 1 ; t<=P ; t++)
	{
		string n,m,dim;
		int N,M;
		getline(input,dim);
		istringstream iss(dim);
		string token;
		getline(iss,token,' ');

		n = token;
		
		getline(iss,token,' ');
		m = token;
		
		N = stoi(n);
		M = stoi(m);
		string** lawn = new string*[N];
		for(int i = 0; i < N; i++)
			lawn[i] = new string[M];
		
		for(int i = 0; i<N; i++)
		{
			string x = "";
			getline(input,x);
			istringstream iss2(x);
			string token2;
			for( int j = 0 ; j<M ; j++)
			{
				 getline(iss2,token2,' ');
				
				 lawn[i][j] = token2;
			}
			
		}
		
		

		
		// row detection
		rowsComplete = true;
		colsComplete = true;
		
		for(int i = 0; i< N ; i++)
		{
			for(int j = 0; j<M ; j++)
			{
				if(lawn[i][j] == "1")
				{
					rowsComplete = true;
					colsComplete = true;
					for(int k = 0; k<M ; k++)
					{
						if(lawn[i][k] != "1")
						{
							rowsComplete = false;
							break;
						}

					}
					
					if(rowsComplete == false){	
						for(int l = 0 ; l < N; l++)
						{
							if(lawn[l][j] != "1")
							{
								colsComplete = false;
								break;
							}
						}
					}
					
				}
					if(rowsComplete == false && colsComplete == false)
						break;
			}
			if(rowsComplete == false && colsComplete == false)
				break;
			
		}
		

			
		if(rowsComplete == false && colsComplete == false)
			output<<"Case #"<<t<<": NO"<<endl;
		
		else 
			output<<"Case #"<<t<<": YES"<<endl;
		
		
		


		

		for(int i = 0; i < N; i++)
			delete[] lawn[i];


		delete[] lawn;

		
		
		

	}
	output.close();
	input.close();
	
	return 0;
}

