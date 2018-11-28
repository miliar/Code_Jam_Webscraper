
#include <iostream>
#include <string>
#include <math.h>
#include <memory.h> 
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;

//#define inFile cin
//#define  outFile cout


int N;
int M;

class grass
{
public:
	int index;
	int height;
	bool flag;
};

grass square[10001];

bool cmp(const grass &a, const grass &b)
{
	return a.height < b.height;
}

int main()
{
	ifstream inFile;
	ofstream outFile;
	inFile.open("B-large.in");
	outFile.open("B-large.out");

	int num_cases;
	inFile>>num_cases;
	char a;		
	inFile.get(a);
	int count = 0;
	for (int j1 = 1; j1 <= num_cases; j1++)
	{

		inFile>>N>>M;
		bool flag = true;
		bool flag1 = true;
		bool flag2 = true;
		for(int i = 0; i != N; i++)
		{
			for (int j = 0; j != M; j++)
			{		
				inFile>>square[i*M + j].height;
				square[i*M + j].index = i*M + j;
				square[i*M + j].flag = false;
			}
		}
		stable_sort(square, square + N*M, cmp);
		outFile<<"Case #"<<j1<<": ";
		for(int i = 0; i != N*M; i++)
		{
			if(flag && square[i].flag == false)
			{
				square[i].flag = true;
				flag1 = true;
				flag2 = true;
				for (int j =0; j != N*M; j++)
				{
					if(square[j].flag == false)
					{
						if (flag1&&(square[j].index%M == square[i].index%M))// |
						{
							if (square[j].height > square[i].height)
							{
								flag1 = false;
							}
						}
						if (flag2&&(square[j].index/M == square[i].index/M))// -
						{
							if (square[j].height > square[i].height)
							{
								flag2 = false;
							}
						}
						if (flag1 == false && flag2 == false)
						{
							outFile<<"NO\n";
							flag = false;
							break;
						}
					}
				}
			}

		}
		if (flag)
			outFile<<"YES\n";

	}
	return 0;
}


