#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;
int main()
{
	int n, i, j, k, addk, addn;
	scanf("%d", &n);
	for(i=1;i<=n;i++)
	{
		int War = 0, DWar = 0;
		addk = 0;
		addn = 0;
		scanf("%d", &k);
		vector <double> Nao(k);
		vector <double> Ken(k);
		for(j=0; j<k; j++)
		{
			scanf("%lf", &Nao[j]);
		}
		for(j=0; j<k; j++)
		{
			scanf("%lf", &Ken[j]);
		}
		sort(Nao.begin(), Nao.end());
		sort(Ken.begin(), Ken.end());
		for(j=0; j<k; j++)
		{
			if(addk == k-1)
			{
				if(Nao[j]>Ken[addk])
				{
					War = k-j;
					break;
				}
				else
				{
					War = k-j-1;
					break;
				}
			}
			while(Nao[j]>Ken[addk])
			{
				addk++;
				if(addk == k-1)
				{
					if(Nao[j]>Ken[addk])
					{
						War = k-j;
						break;
					}
					else
					{
						War = k-j-1;
						break;
					}
				}
			}
			if(War)
			{
				break;
			}
			addk++;
		}
		for(j=0; j<k; j++)
		{
			if(addn == k-1)
			{
				if(Ken[j]>Nao[addn])
				{
					DWar = j;
					break;
				}
				else
				{
					DWar = j+1;
					break;
				}		
			}
			while(Ken[j]>Nao[addn])
			{
				addn++;
				if(addn == k-1)
				{
					if(Ken[j]>Nao[addn])
					{
						DWar = j;
						break;
					}
					else
					{
						DWar = j+1;
						break;
					}
					
				}
			}
			if(DWar)
			{
				break;
			}
			addn++;
		}
		printf("Case #%d: %d %d\n", i, DWar, War);
	}
	return 0;
}
