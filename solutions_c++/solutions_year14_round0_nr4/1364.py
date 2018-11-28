/*GOOGLE CODE JAM
 *ANDREW WILKENING
 *APRIL 11, 2014
 *PROBLEM D - COOKIE CLICKER ALPHA
 */

#include<fstream>
#include<iostream>
#include<iomanip>
#include<algorithm>
#include<vector>

using namespace std;

int main()
{
	ifstream fin("LargeD.in");
	ofstream fout("LargeDSol.out");
	vector<double> Naomi, DNaomi;
	vector<double> Ken, DKen;
	double tell, temp;
	vector<double>::iterator NChosen, KChosen;
	int DWar, War, runs, N;
	fin >> runs;
	for(int i = 1; i <= runs; i++)
	{
		DWar = 0;
		War = 0;
		fin >> N;
		for(int j = 0; j < N; j++)
		{
			fin >> temp;
			Naomi.push_back(temp);
		}
		for(int j = 0; j < N; j++)
		{
			fin >> temp;
			Ken.push_back(temp);
		}
		sort(Naomi.begin(), Naomi.end());
		sort(Ken.begin(), Ken.end());
		DNaomi = Naomi;
		DKen = Ken;
		//WAR
		for(int j = 0; j < N; j++)
		{
			NChosen = Naomi.end() - 1;
			KChosen = Ken.begin();
			for(int k = 0; k < Ken.size(); k++)
			{
				if(Ken[k] > *NChosen) k = Ken.size();
				else KChosen++;
			}
			Naomi.erase(NChosen);
			if(KChosen == Ken.end())
			{
				Ken.erase(Ken.begin());
				War++;
			}
			else Ken.erase(KChosen);
		}
				
		//DECEITFUL WAR
		for(int j = 0; j < N; j++)
		{
			NChosen = DNaomi.end() - 1;
			KChosen = DKen.end() - 1;
			if(*NChosen < *KChosen)
			{
				DNaomi.erase(DNaomi.begin());
				DKen.erase(DKen.end()-1);
			}
			else
			{
				KChosen = DKen.begin();
				while(*NChosen > *KChosen)
				{
					NChosen--;
				}
				NChosen++;
				DNaomi.erase(NChosen);
				DKen.erase(KChosen);
				DWar++;
			}
		}
		fout << "Case #" << i << ": " << DWar << " " << War << endl;
	}
	return 0;
}
