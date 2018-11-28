#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <conio.h>
#include <algorithm>
#include "Windows.h"

using namespace std;

typedef struct {
	int Value;
		int Index;
} Node;

int main()
{
	LARGE_INTEGER frequency;        // ticks per second
	LARGE_INTEGER t1, t2;           // ticks
	double elapsedTime;

	// get ticks per second
	QueryPerformanceFrequency(&frequency);

	// start timer
	QueryPerformanceCounter(&t1);

	string line;
	const string Path("E:\\personal\\");
	string mInFileName(Path + "A-large.in");
	ifstream myfile;
	myfile.open(mInFileName.c_str());
	int idx;
	//////////////////////////////Specific Var///////////////////////////////
	int mLoop=0;
	string ShyMax , ShyLevel;
	int Fi, mShyMax;
	int SumShy, SumNum;
	int Diff, TotalSum;
	string temp;
	string mOutFileName(Path + "A-large.out");
	ofstream myfile1 ( mOutFileName.c_str());
	/////////////////////////////////////////////////////////////////////////
	//////////////////////////////Reading file///////////////////////////////
	
	  if (myfile.is_open())
	  {
		  if(getline (myfile,line))
		  {
			  mLoop = atoi(line.c_str());
		  }
		 
		for(idx = 0; idx < mLoop; idx++)
		{			
				
				if(getline(myfile,line))
				{
					istringstream iss(line);
					if(iss)
					{
						
						iss >> ShyMax;
						iss >> ShyLevel;
						mShyMax = atoi(ShyMax.c_str());
					} 
					
					int i=0;
					Fi = 1;
					SumShy = 1;
					SumNum = 0;
					Diff = 0;
					TotalSum = 0;
					for(i=0;i<ShyLevel.size();i++)
					{
						temp = ShyLevel[i];
						Fi = atoi(temp.c_str());
						
						//swap(SumShy,Fi);
						//SumShy = SumShy + Fi;
						if( ((i) > SumNum )&&(Fi!=0) )
						{
							Diff = i - SumNum;
							SumNum = SumNum + Diff;
							TotalSum = Diff + TotalSum;
						}
						SumNum = SumNum + Fi;
						
					}
					/*if(mShyMax>SumNum)
					{
						TotalSum = TotalSum + mShyMax - SumNum;
					}*/
				
				}
				else return -1;
				if (myfile1.is_open())
				 {
					 myfile1 << "Case #"<<idx + 1<<": " <<TotalSum<<endl;
				 }
		///////////////////////////////////////////////////////////
			
			
		}
		myfile.close();
	  }

	  else cout << "Read::Unable to open file"; 
	///////////////////////////////////////////////////////////////////////////

	////////////////////////////Writing File///////////////////////////////////
	  
	  
		myfile1.close();
	///////////////////////////////////////////////////////////////////////////
	  // stop timer
	QueryPerformanceCounter(&t2);
	// compute and print the elapsed time in millisec
	elapsedTime = (t2.QuadPart - t1.QuadPart) * 1000.0 / frequency.QuadPart;
	cout << elapsedTime;
	getch();
	return 0;
}