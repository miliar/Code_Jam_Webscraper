//infinite house of pancake
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

vector<int> pecah(vector<int> P, int j);

int main() {
	int t, D, a;
	
	scanf("%d",&t);
	for (int z=1; z<=t; z++) 
	{	
		scanf("%d",&D);
		vector<int> P;
		int time = 0;
		
		for (int i=0; i<D; i++) 
		{
			scanf("%d",&a);
			P.push_back(a);
		}
		sort(P.begin(), P.end(), std::greater<int>());
		
		int upperBound = P[0];
		time = upperBound;
		
		vector< vector<int> > table;
		table.push_back(P);
		
		
		//printout
			/*printf("Printout 1\n");
			for (int i=0; i<table.size(); i++)
			{
				for (int k=0; k<table[i].size(); k++)
					printf("%d ",table[i][k]);
				printf("\n");
			}
			printf("--------\n\n");*/
		
		//
		bool flag = false;
		for (int k=1; k<=upperBound && !flag; k++)
		{
			//collector
			for (int i=0; i<table.size(); i++)
			{
				//printf("%d %d\n",table[i].size(), table[i][table[i].size()-1]);
				while (table[i].size()>0 && table[i][table[i].size()-1] == 0)
				{
					//printf("pop back table %d\n",i);
					table[i].pop_back();
				}
				
				if (table[i].size()==0)
				{
					//printf("raise flag here\n");
					//getchar();
					flag = true;
					time = k-1;
				}
			}
			
			//kurangi
			if (!flag)
			{
				int len = table.size();
				//printf("table size = %d\n",len);
				
				//kasus jika dipecah
				for (int i=0; i<len; i++)
				{
					if (table[i][0] > 1)
					{
						for (int j=1; j<=table[i][0]/2; j++) {
							table.push_back(pecah(table[i],j));
						}
					}
				}	
				//kasus jika dikurangi
				for (int i=0; i<len; i++)
				{
					for (int j=0; j<table[i].size(); j++)
						table[i][j] -= 1;
				}
			}
			
			//printout
			/*printf("Printout %d\n",k);
			for (int i=0; i<table.size(); i++)
			{
				for (int j=0; j<table[i].size(); j++)
					printf("%d ",table[i][j]);
				printf("\n");
			}
			printf("--------\n\n");
			getchar();*/
		}
		//
		printf("Case #%d: %d\n",z, time);
	}
	return 0;
}

vector<int> pecah(vector<int> P, int j)
{
	vector<int> temp2 = P;
	/*int temp = temp2[0] / 2;
	temp2.push_back(temp);
	temp2[0] = temp2[0] - temp;*/
	temp2[0] -= j;
	temp2.push_back(j);
	sort(temp2.begin(), temp2.end(), std::greater<int>());
	
	return temp2;
}
