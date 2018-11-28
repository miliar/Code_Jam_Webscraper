//#include "stdafx.h"
#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
#include <algorithm>

using namespace std;

int main()
{
	int N; 
	int ii,j,k,testn,id;	

	//int r1, r2, arr1[N][N]={0}, arr2[N][N]={0};
	//int mat[R][C], cmat[R][C] = {{0},{0}};	
	double* narr;
	double* karr;
	double* ckarr;
	ifstream readfile ;
	readfile.open("D-large.in");
	readfile >> testn;
	
	//cin >> testn;
	//int* val = new int[testn];
	int co = 0, found = 0;
	ofstream myfile;
	myfile.open ("q4.txt");
	
	for(ii=0; ii<testn; ii++)
	{		
		co = 0; 
		double nn,kn;
		//s =0, t1 = 0, t1c = 0, t2 = 0, ss = 0;
		readfile >> N;		
		narr = new double[N];
		karr = new double[N];
		ckarr = new double[N];
		for(j=0;j<N;j++)
		{
			readfile >> narr[j];			
		}
		for(j=0;j<N;j++)
		{
			readfile >> karr[j];			
		}		
		//std::sort(
		std::sort(narr,narr+N);
		std::sort(karr,karr+N);
		
		for(j=0;j<N;j++)
		{
			//cout << narr[j] << " ";		
			ckarr[j] = karr[j];
		}
		
		//cout << endl;
		//optimal play by naomi
		for(j=N-1;j>=0;j--)			
		{				
			nn = narr[j];			
			found = 0;
			for(k=0;k<N;k++)
			{
				if ((karr[k]>nn) && (karr[k] != 0))
				{
					kn = karr[k];
					found = 1;
					karr[k] = 0;
					break;
				}
			}
			if(found != 1)
			{
				co++;
				for(k=0;k<N;k++) {
					if (karr[k] != 0)
					{
						karr[k] = 0;
						break;
					}
				}
			}			
		}		
		
		//cout << "points optimal:" << co << endl;
		//deceitful game
		int last=0;
		k=0;
		int cd = 0;
		int flag = 0;
		for(j=0;j<N ;j++)
		{	
			if(narr[j] > ckarr[k])
			{				
				cd++;
				k++;
			}			

		}
		//cout << endl << cd << " "<< co ;



		
		myfile  << "Case #" << ii+1 << ": " << cd << " " << co << endl;			
			
			
			//myfile << endl;
			//cout << endl;
		}

	myfile.close();
	return(0);
}
