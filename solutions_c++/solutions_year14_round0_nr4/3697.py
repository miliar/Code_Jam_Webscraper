#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
	//freopen("input.txt", "r", stdin);
	freopen("test2.in", "r", stdin);
	freopen("output2.txt", "w", stdout);

	int testCases;
	scanf("%d", &testCases);
	for (int a=0; a<testCases; a++)
	{
		int totalBlocks;
		scanf("%d", &totalBlocks);
		vector <double> naomi(totalBlocks);
		vector <double> ken(totalBlocks);
		vector <bool> kenUsed(totalBlocks,false);
		for (int c=0; c<totalBlocks; c++)
		 cin >> naomi[c];
		for (int c=0; c<totalBlocks; c++)
			cin >> ken[c];
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		int originalScore=0;
		int lastKenBlock=0;
		for (int d=0; d<totalBlocks; d++)
		{
			bool found=false;
			for (int cc=lastKenBlock; cc<totalBlocks; cc++)
			{
				if (kenUsed[cc]) continue;
				if (ken[cc]>naomi[d])
				{
					found=true;
					kenUsed[cc]=true;
					lastKenBlock=cc;
					break;
				}
			}
			if (!found) originalScore++;
		}
		int currentKenBlock=totalBlocks-1;
		int newBestScore=0;
		int resolved=0;
		int lastBlock=0;
		int newLastKenBlock=0;
		kenUsed=vector <bool> (totalBlocks,false);
		for (int c=0; c<totalBlocks; c++)
		{
			bool found=false;
			for (int dd=newLastKenBlock; dd<totalBlocks; dd++)
			{
				if (kenUsed[dd]) continue;
				if (naomi[c]>ken[dd])
				{
					kenUsed[dd]=true;
					newBestScore++;
					newLastKenBlock=dd;
					found=true;
					break;
				}
				if (!kenUsed[dd]) break;
			}


			if (found) continue;
			for (int dd=totalBlocks-1; dd>=0; dd--)
			{
				if (kenUsed[dd]) continue;
				if (ken[dd]>naomi[c])
				{
					kenUsed[dd]=true;
					found=true;
					break;
				}
				
			}
			if(!found) 
			{
				//newBestScore++;
				newBestScore+=(totalBlocks-c);
				break;
			}

		}


		printf("Case #%d: %d %d\n", a+1, newBestScore,originalScore);
		/*
		for (int d=0; d<totalBlocks; d++)
		{
			printf("%.3f ", naomi[d]);
		}
		cout << endl;
		for (int d=0; d<totalBlocks; d++)
		{
			printf("%.3f ", ken[d]);
		}
		cout << endl;*/


	}




}