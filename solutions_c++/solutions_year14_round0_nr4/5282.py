#include <iostream>
#include <string>
#include <fstream>
#include <set>
using namespace std;

int main()
{
	ofstream fsout("result3.txt");
	int caseTime = 0;
	cin>>caseTime;

	for (int times = 0;times < caseTime;times++)
	{
		char temp[10];
		itoa(times+1,temp,10);
		fsout<<"Case #"+(string)temp+": ";
		int numberOfBlocks = 0;
		cin>>numberOfBlocks;

		bool getDeceit = false;
		bool getOptimal = false;
		int optimal = 0;
		
// 		double massOfMaoniBlocks[10];
// 		double massOfKenBlocks[10];

// 		double *massOfMaoniBlocks;
// 		double *massOfKenBlocks;
// 
//  		massOfMaoniBlocks = (double *)malloc(sizeof(double)*numberOfBlocks);
//  		massOfKenBlocks = (double *)malloc(sizeof(double)*numberOfBlocks);

		set<double> massOfMaoniBlocks,massOfKenBlocks;
		set<double> massOfMaoniBlocksOptimal,massOfKenBlocksOptimal;

		double temp1,temp2;
		for (int i = 0;i < numberOfBlocks;i++)
		{
			cin>>temp1;
			massOfMaoniBlocks.insert(temp1);
			massOfMaoniBlocksOptimal.insert(temp1);
		}

		for (int i = 0;i < numberOfBlocks;i++)
		{
			cin>>temp2;
			massOfKenBlocks.insert(temp2);
			massOfKenBlocksOptimal.insert(temp2);
		}

		/////deceitful
		while(!getDeceit)
		{
			if (massOfKenBlocks.size() == 0)
			{
				getDeceit = true;
			}
			set<double>::iterator iter = massOfMaoniBlocks.begin();
			for (int i = 0;i < massOfKenBlocks.size();)
			{
				bool allLarge = true;
				set<double>::iterator iterOfMaoni = massOfMaoniBlocks.begin();
				set<double>::iterator iterOfKen = massOfKenBlocks.begin();
				for (;iterOfMaoni != massOfMaoniBlocks.end();iterOfMaoni++,iterOfKen++)
				{
					if (*iterOfMaoni >= *iterOfKen)
					{
						continue;
					}
					else
					{
						allLarge = false;
						break;
					}
		//			allLarge = true;
				}
				if (!allLarge)
				{
					if (massOfMaoniBlocks.size() > 0)
					{
						set<double>::iterator iter = massOfMaoniBlocks.begin();
						set<double>::iterator iter1 = massOfKenBlocks.end();
						massOfMaoniBlocks.erase(iter);
						massOfKenBlocks.erase(--iter1);
					}
				}
				else
				{
					getDeceit = true;
					break;
				}
			}
		}
		fsout<<massOfKenBlocks.size()<<" ";

		//optimal
		set<double>::iterator iterOfMaoni = massOfMaoniBlocksOptimal.end();
		for (int i = 0;i < massOfMaoniBlocksOptimal.size();)
		{
			bool allSmall = true;
			set<double>::iterator iterOfKen = massOfKenBlocksOptimal.begin();
			for (;iterOfKen != massOfKenBlocksOptimal.end();iterOfKen++)
			{
				if (*iterOfKen > *(-- massOfMaoniBlocksOptimal.end()))
				{
					massOfMaoniBlocksOptimal.erase(--massOfMaoniBlocksOptimal.end());
					massOfKenBlocksOptimal.erase(iterOfKen);
					allSmall = false;
					break;
				}
				else
				{
					continue;
				}

			}
			if (allSmall)
			{
				optimal++;
				massOfMaoniBlocksOptimal.erase(--massOfMaoniBlocksOptimal.end());
				massOfKenBlocksOptimal.erase(massOfKenBlocksOptimal.begin());
			}
		}
		fsout<<optimal<<endl;
	}

	fsout.close();
	return 0;
}