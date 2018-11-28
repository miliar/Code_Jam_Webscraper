/*
 * sample.cpp
 *
 *  Created on: Apr 11, 2015
 *      Author: ttcn
 */

#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <sstream>
#include <numeric>

using namespace std;

#include <numeric>

int gcd(int a, int b)
{
    for (;;)
    {
        if (a == 0) return b;
        b %= a;
        if (b == 0) return a;
        a %= b;
    }
}

int lcm(int a, int b)
{
    int temp = gcd(a, b);

    return temp ? (a / temp * b) : 0;
}


int main()
{
	fstream infile,outfile;
	infile.open("B-small-attempt2.in", ios::in );
	outfile.open("B-small-attempt2.out", ios::out | ios::trunc );

	int numOfinputs = 0;

	infile>>numOfinputs;
    cout<<"numOfinputs:" << numOfinputs << endl;

    // table for winning

	for(int i=0; i<numOfinputs; i++)
	{
		int N;
		unsigned long long  Q;
		vector<int> M;
		vector<int> MTime;


		int j,k;
		infile >> N;
		infile >> Q;

		int Max = 0;

		for(j=0; j < N; j++)
		{
			int Mi;
			infile >>Mi;
			M.push_back(Mi);
			MTime.push_back(0);
		}

		int LCMValue = std::accumulate(M.begin(), M.end(), 1, lcm);
		cout<<"LCM"<<LCMValue;

		unsigned long long Modulo = 0;
		for(j=0; j < N; j++)
		{
			Modulo+= (LCMValue/M[j]);
		}
		cout<<"Mod"<<Modulo;

		outfile << "Case #" << i+1 << ": ";

		//int  = 0;
		//skip the last
		int LastIndex = 0;
		unsigned int MAX = 0x0FFFFFFF;
		unsigned long long l;
		int n= ((Q-1)%Modulo);
		for(l=0; l < n+1; l++)
		{
			unsigned int lowestTime = MAX;
			int Index=0;

			for(k=0; k<N;k++)
			{
				if(lowestTime > MTime[k])
				{
					lowestTime = MTime[k];
					Index = k;
				}
			}

			MTime[Index] +=M[Index];
			LastIndex = Index;
		}
		cout << LastIndex+1<<endl;
		outfile <<LastIndex+1<<endl;
	}

	return 1;
}


