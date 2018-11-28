#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

#define FILE_NAME "D-large"
#define ULL unsigned long long

char buffer[2048];

vector<double> naomi;
vector<double> ken;

int main()
{
	sprintf(buffer, "%s.in", FILE_NAME);
	freopen(buffer, "r", stdin);
	sprintf(buffer, "%s.out", FILE_NAME);
	freopen(buffer, "w", stdout);

	int case_num, N;
	int i=1;
	scanf("%d", &case_num);
	while(i<=case_num)
	{
		printf("Case #%d: ", i);
		
		scanf("%d", &N);
		naomi.clear();
		ken.clear();
		double num;
		for(int m=0;m<2;m++)
		{
			for(int n=0;n<N;n++)
			{
				scanf("%lf", &num);
				if(m==0)
					naomi.push_back(num);
				else
					ken.push_back(num);
			}
		}

		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		vector<double> cloneKen = vector<double>(ken.begin(), ken.end());
		int Z = 0;
		for(int j=0;j<N;j++)
		{
			double chosenNaomi = naomi[j];
			vector<double>::iterator it;
			bool couldWin = false;
			for(it=cloneKen.begin();it<cloneKen.end();it++)
			{
				if((*it)>chosenNaomi)
				{
					cloneKen.erase(it);
					couldWin = true;
					break;
				}
			}
			if(!couldWin)
			{
				cloneKen.erase(cloneKen.begin());
				Z++;
			}
		}
		int Y = 0;
		reverse(naomi.begin(), naomi.end());
		reverse(ken.begin(), ken.end());
		for(int j=0;j<N;j++)
		{
			double chosenNaomi = naomi[j];
			if(ken.size()>1)
			{
				bool couldWin = false;
				vector<double>::iterator it;
				for(it=ken.begin();it<ken.end();it++)
				{
					if(chosenNaomi>(*it))
					{
						ken.erase(it);
						couldWin = true;
						break;
					}
				}
				if(couldWin)
					Y++;
				//else
				//	ken.erase(ken.begin());
			}
			else
			{
				if(chosenNaomi>ken.front())
					Y++;
			}
		}

		printf("%d %d", Y, Z);

		printf("\n");
		i++;
	}
		
	return 0;
}