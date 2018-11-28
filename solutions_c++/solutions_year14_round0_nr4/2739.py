// CodeJam_QR14_04.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <algorithm>

#define FIRST 0
#define SECOND 1

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

const int PlayersNumber=2,MaxBlocksAmount=1000000;

int BlocksAmount,Ans1,Ans2;
double WeightsF[MaxBlocksAmount],WeightsS[MaxBlocksAmount],WeightsF1[MaxBlocksAmount],WeightsS1[MaxBlocksAmount];

void Solve()
{
	Ans1=Ans2=0;					//the DWar and WAR points
	int look=BlocksAmount-1;
	sort(WeightsF,WeightsF+BlocksAmount);
	sort(WeightsS,WeightsS+BlocksAmount);

	for (int i=0;i<BlocksAmount;i++)	//cant believe I'm writing this
		WeightsF1[i]=WeightsF[i],WeightsS1[i]=WeightsS[i];


	for (int Try=0,i;Try<BlocksAmount;Try++)
	{
		if (WeightsF[look]>WeightsS[look])
		{
			for (i=look;i>Try && WeightsF[i-1]>WeightsS[look];i--)
				;
			WeightsF[i]=WeightsS[look]=0,Ans1++;
		}
		//if (WeightsF[Try]>WeightsS[look])
		//	WeightsF[Try]=WeightsS[look]=0,Ans1++;
		else
			WeightsF[Try]=WeightsS[look]=0;
		sort(WeightsF,WeightsF+BlocksAmount);
		sort(WeightsS,WeightsS+BlocksAmount);
	}


	for (int Try=0;Try<BlocksAmount;Try++)
	{
		if (WeightsF1[look]>WeightsS1[look])
			WeightsF1[look]=WeightsS1[Try]=0,Ans2++;
		else
			WeightsF1[look]=WeightsS1[look]=0;
		sort(WeightsF1,WeightsF1+BlocksAmount);
		sort(WeightsS1,WeightsS1+BlocksAmount);
	}

	fout << Ans1 << " " << Ans2 << "\n";
		//for (look=BlocksAmount-1;look>=Try;look--)
			//if (WeightsF[Try]<WeightsS[look])

}

int main()
{
	int c;
	fin >> c;
	for (int m=1;m<=c;m++)
	{
		fin >> BlocksAmount;
		for (int i=0;i<BlocksAmount;i++)
			fin >> WeightsF[i];
		for (int i=0;i<BlocksAmount;i++)
			fin >> WeightsS[i];
		fout << "Case #" << m << ": ";
		Solve();
	}
	return 0;
}

