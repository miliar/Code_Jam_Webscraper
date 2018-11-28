#include <iostream>
#include <fstream>
#include <set>
#include <cmath>
#include <algorithm>
using namespace std;

//istream& fin = cin;
//ifstream fin ("D-sample.txt");
//ifstream fin ("D-small-attempt0.in");
ifstream fin ("D-large.in");
//ofstream fout ("D-small-attempt0.out");
ofstream fout ("D-large.out");
//ostream& fout = cout;

int main()
{
	int N, T;
	double weight;

	fin >> N;
	for(int n=1; n<=N; n++)
	{
		set<double> block[2];
		int war = 0;
		int dWar = 0;
		
		fin >> T;
		for(int k=0; k<2; k++)
		{			
			for(int i=0; i<T; i++)
			{
				fin >> weight;
				block[k].insert(weight);
			}
		}
		
		/*
		// print sorted
		for(auto it1=block[0].begin(),
			it2=block[1].begin();
			it2 != block[1].end();
			it1++,it2++)
		{
			double w1 = *it1;
			double w2 = *it2;
			cout << w1 << "\t" << w2 << endl;
		}
		*/
		
		// deceitful war game
		for(auto it1=block[0].rbegin(),
			it2=block[1].rbegin();
			it2 != block[1].rend();
			)
		{
			double w1 = *it1;
			double w2 = *it2;
			if(w1 > w2)
			{
				dWar++;
				it1++;
				it2++;
			}
			else
			{
				it2++;
			}
		}
		
		// war game
		for(auto it1=block[0].begin(); it1 != block[0].end(); it1++)
		{
			double w1 = *it1;
			auto it2 = lower_bound(block[1].begin(),block[1].end(),w1);
			if(it2==block[1].end())
			{
				war++;
				block[1].erase(block[1].begin());				
			}
			else
			{
				block[1].erase(it2);
			}
		}
		
		fout << "Case #" << n << ": ";
		fout << dWar << " " << war;
		fout << endl;
	}
	
	return 0;
}

