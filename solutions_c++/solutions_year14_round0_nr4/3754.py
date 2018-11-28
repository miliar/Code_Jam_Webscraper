#include <cstdlib>
#include <iostream>
#include <string.h>
#include <vector>
#include <stdio.h>
#include <fstream>
using namespace std;

ofstream myAns;
ifstream Qfile;

void shellsort(double *data, size_t size)
{
    for (int gap = size / 2; gap > 0; gap /= 2)
        for (int i = gap; i < size; ++i)
        {
 
             double key = data[i];
             int j = 0;
             for( j = i -gap; j >= 0 && data[j] > key; j -=gap)
             {
                data[j+gap] = data[j];
              }  
             data[j+gap] = key;
         }
}

void Solve(int CaseNum)
{
	int N;
	double NaomiBlocks[1000];
	double KenBlocks[1000];
	int i;
	int WarPoint=0;
	int DeceitfulWarPoint=0;

	int NaomiSmallIndex=0;
	int NaomiBigIndex=0;

	int KenSmallIndex=0;
	int KenBigIndex=0;


	Qfile>>N;
	KenBigIndex=N-1;
	NaomiBigIndex=N-1;
	

	for(i=0; i<N; i++) Qfile>>NaomiBlocks[i];
	for(i=0; i<N; i++) Qfile>>KenBlocks[i];

	shellsort(NaomiBlocks,N);
	shellsort(KenBlocks,N);

	for(i=N-1;i>=0;i--)
	{
		if(NaomiBlocks[NaomiBigIndex]>KenBlocks[KenBigIndex])
		{
			WarPoint++;
			NaomiBigIndex--;
			KenSmallIndex++;
		}
		else
		{
			NaomiBigIndex--;
			KenBigIndex--;
		}
	}


	KenSmallIndex=0;
	KenBigIndex=0;
	KenBigIndex=N-1;
	NaomiBigIndex=N-1;

	for(i=0;i<N;i++)
	{
		if(NaomiBlocks[NaomiSmallIndex]>KenBlocks[KenSmallIndex])
		{
			DeceitfulWarPoint++;
			NaomiSmallIndex++;
			KenSmallIndex++;
		}
		else
		{
			NaomiSmallIndex++;
			KenBigIndex--;
		}
	}


	myAns<<"Case #"<<CaseNum<<": ";
	myAns<< DeceitfulWarPoint <<" ";
	myAns<< WarPoint;
	myAns<<endl;
}

int main(int argc, char *argv[])
{
	int T=0;
	int i=0;

	Qfile.open("D-large.in");
	myAns.open ("MyAnser.txt");
		
	Qfile>>T;	
	
	for(i=0; i<T; i++)	
	{						
		Solve(i+1);
	}
	myAns.close();
	Qfile.close();
    
	system("PAUSE");
    return EXIT_SUCCESS;
}
