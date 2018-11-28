#include <iostream>
#include <fstream>
#include <stdlib.h>
using namespace std;

int compare (const void * a, const void * b)
{
	float p1, p2;
	p1 = *(float*)a;
	p2 = *(float*)b;
	
	if ( p1 < p2 )
	{
		return -1;
	}
	else if (p2 < p1)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

void main()
{
	std::ifstream ifs ("input.txt", std::ifstream::in);
	int tests;
	ifs>>tests;
	ofstream myfile;
	myfile.open ("output.txt");
	
	for(int i=1;i<=tests;i++)
	{
		int N;
		ifs>>N;
		float *Naomi = new float[N];
		float *Ken   = new float[N];
		bool* KenUsed = new bool[N];
		for(int j=0;j<N;j++)
		{
			ifs>>Naomi[j];
		}
		for(int j=0;j<N;j++)
		{
			ifs>>Ken[j];
			KenUsed[j] = false;
		}

		int y = 0;
		int z = 0;

		qsort (Naomi, N, sizeof(float), compare);
		qsort (Ken, N, sizeof(float), compare);
		
		for(int j = 0;j<N;j++)
		{
			bool found = false;
			int minPos = N;
			for(int k=0;k<N;k++)
			{
				if(!KenUsed[k])
				{
					if(k < minPos)
					{
						minPos = k;
					}
					if(Ken[k] > Naomi[j])
					{
						KenUsed[k] = true;
						found = true;
						break;
					}
				}
			}
			if( ! found )
			{
				KenUsed[minPos] = true;
				z++;
			}
		}

		int NfrontDW = 0;
		int NbackDW = N-1;
		int KbackDW = N-1;
		for(int j = N-1;j>=0;j--)
		{
			if(Naomi[NbackDW] > Ken[KbackDW])
			{
				NbackDW--;
				KbackDW--;
				y++;
			}
			else
			{
				NfrontDW++;
				KbackDW--;
			}
		}

		myfile << "Case #"<<(i)<<": "<<y<<" "<<z;
		myfile<<"\r\n";

		delete[] Naomi;
		delete[] Ken;
	}
	ifs.close();
	myfile.close();
}