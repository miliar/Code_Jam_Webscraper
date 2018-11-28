#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
	ofstream fout;
	ifstream fin;
	fout.open("results.txt");
	fin.open("input.txt");
	int cases, test = 1, blocks, kFirst, kLast, dScore, wScore;
	double naomi[1000] = {};
	double ken[1000] = {};

	fin>>cases;

	while(test <= cases)
	{
		fin>>blocks;

		dScore = 0;
		wScore = 0;
		kFirst = 0;
		kLast = blocks - 1;

		for(int k = 0; k < blocks; k++)
			fin>>naomi[k];
		for(int k = 0; k < blocks; k++)
			fin>>ken[k];

		sort(naomi, naomi+blocks);
		sort(ken, ken+blocks);

		for(int k = 0; k < blocks; k++)
		{
				if(ken[kFirst] <= naomi[k])
				{
					dScore++;
					kFirst++;
				}
				else
					kLast--;
		}

		kFirst = 0;

		for(int k = 0; kFirst < blocks; k++)
		{
			while(ken[kFirst] < naomi[k] && kFirst < blocks)
			{
				kFirst++;
				wScore++;
			}

			kFirst++;
		}

		fout<<"Case #"<<test<<": "<<dScore<<" "<<wScore<<endl;
		test++;
	}



	return 0;
}
