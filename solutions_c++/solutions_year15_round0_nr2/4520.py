#include <iostream>
#include <cstdio>
#include <cstdlib>
//#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int T; //test case number
vector<int> Diner;
int input;
//int TotalCakes;
int BestTime;

int findMatch(vector<int> v, int N)
{
	int i;
	int match = 0;
	for(i=0;i<v.size();i++)
	{
		if(v[i] == N)
		{
			match++;
		}
	}
	return match;
}

void solve(vector<int> &Diner, int moveTime, int DNumber)
{
	int temp;
	int n = Diner[DNumber-1];
	DNumber++;
	moveTime++;

	for(int cakeAmount=1;cakeAmount<=(n/2);cakeAmount++)
	{
		vector<int> DinerTemp(Diner.begin(),Diner.end());

		DinerTemp[DNumber-2] -= cakeAmount;
		DinerTemp.push_back(cakeAmount);
		sort(DinerTemp.begin(), DinerTemp.end());
		temp = DinerTemp[DNumber-1] + moveTime;
		if(temp < BestTime)
		{
			BestTime = temp;
			//solve(DinerTemp, moveTime, DNumber);
		}

		if(DinerTemp[DNumber-1] <= 3)
        {
            continue;
        }

        if(((n/2 + 1) + findMatch(DinerTemp, DinerTemp[DNumber-1])) >=  n)
        {
            continue;
        }

		solve(DinerTemp, moveTime, DNumber);
	}

	return;
}

int main()
{
	int iCase = 0;
	FILE *fp_r, *fp_w;
	if((fp_r = fopen("B-small-attempt7.in", "r")) == NULL)
	{
		exit(-1);
	}
	if((fp_w = fopen("B-small-attempt7.out", "w")) == NULL)
	{
		exit(-1);
	}
	fscanf(fp_r, "%d", &T); //test case number
	printf("T = %d\n", T);

	while(T--)
	{
		cout << "#####T=" << T << "\n";
		int DNumber = 0;
		BestTime = 0;
		int i;
		Diner.clear();
		fscanf(fp_r, "%d", &DNumber);
		for(i=0;i<DNumber;i++)
		{
			fscanf(fp_r, "%d", &input);
			Diner.push_back(input);
			//TotalCakes += Diner[i];
		}
		/*for(vector<int>::iterator it = Diner.begin(); it != Diner.end(); it++)
		{
			printf("%d\t", *it);
		}
		printf("\n");*/

		//start to solve problem
		sort(Diner.begin(), Diner.end());
		BestTime = Diner[DNumber-1];

		solve(Diner, 0, DNumber);



		/////output/////
		fprintf(fp_w, "Case #%d: %d\n", ++iCase, BestTime);
	}

	fclose(fp_r);
	fclose(fp_w);
	return 0;
}

