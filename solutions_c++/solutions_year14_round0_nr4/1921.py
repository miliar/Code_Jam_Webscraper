#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <functional>
#include <queue>
FILE *in = fopen("D-large.in", "r");
FILE *out = fopen("output.txt", "w");
int n = 1;

void testCase()
{
	//input
	int N;;
	fscanf(in, "%d", &N);
	double dOriginalNaomi[1001];
	double dOriginalKen[1001];
	for(int i=0; i<N; ++i)
	{
		fscanf(in, "%lf", &dOriginalNaomi[i]);
	}
	for(int i=0; i<N; ++i)
	{
		fscanf(in, "%lf", &dOriginalKen[i]);
	}
	int ans1, ans2;
	{
		std::vector<double> vNaomi;
		std::vector<double> vKen;

		for(int i=0; i<N; ++i)
		{
			vNaomi.push_back(dOriginalNaomi[i]);
			vKen.push_back(dOriginalKen[i]);
		}
		std::stable_sort(vNaomi.begin(), vNaomi.end());
		std::stable_sort(vKen.begin(), vKen.end());
		int winCounter = 0;

		for(int i=0; i<N; ++i)
		{
			if( vNaomi.front() < vKen.front() )
			{
				vNaomi.erase(vNaomi.begin());
				vKen.pop_back();
			}
			else
			{
				winCounter++;
				std::vector<double>::iterator saver;
				double naomi = vNaomi.front();
				for(std::vector<double>::iterator it = vKen.begin(); it!= vKen.end(); it++)
				{
					if(*it < naomi)
					{
						saver = it;
					}
					else break;
				}
				vNaomi.erase(vNaomi.begin());
				vKen.erase(saver);
			}
		}
		ans1 = winCounter;
	}
	{
		
		std::vector<double> vNaomi;
		std::vector<double> vKen;

		for(int i=0; i<N; ++i)
		{
			vNaomi.push_back(dOriginalNaomi[i]);
			vKen.push_back(dOriginalKen[i]);
		}
		std::stable_sort(vNaomi.begin(), vNaomi.end());
		std::stable_sort(vKen.begin(), vKen.end());
		int winCounter = 0;
		for(int i=0; i<N; ++i)
		{
			if( vNaomi.back() > vKen.back() )
			{
				vNaomi.pop_back();
				vKen.erase(vKen.begin());
				winCounter++;
			}
			else
			{
				double naomi = vNaomi.back();
				double tmp;
				std::vector<double>::iterator saver;
				for(std::vector<double>::iterator it = vKen.begin(); it != vKen.end(); it++)
				{
					
					if( naomi < *it )
					{
						tmp = *it;
						saver = it;
						break;
					}
				}
				vNaomi.pop_back();
				vKen.erase(saver);
			}
		}
		ans2 = winCounter;
	}
	fprintf(out, "Case #%d: %d %d", n++, ans1, ans2);
	fprintf(out, "\n");
}
int main(void)
{
	int tCase;
	fscanf(in, "%d",&tCase);
	while(tCase--)
	{
		testCase();
	}	
}