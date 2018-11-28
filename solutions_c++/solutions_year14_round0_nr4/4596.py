#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

int main(void)
{
	int n;
	scanf("%d",&n);
	int t;
	for(int i=1; i<=n; i++)
	{
		scanf("%d",&t);
		
		vector<float> naomi(t,0.0), dnao(t,0.0);
		vector<float> ken(t,0.0), dken(t,0.0);
		
		for(int j=0; j<t; j++)
			scanf("%f",&naomi[j]);
		for(int j=0; j<t; j++)
			scanf("%f",&ken[j]);
		sort(naomi.begin(),naomi.end(),greater<float>());
		sort(ken.begin(),ken.end(),greater<float>());
		
		dnao = naomi;
		dken = ken;
		
		int war = 0, dwar = t;
		for(int k=0; k<t; k++)
		{
			bool flag = false;
			for(int j=0; j<ken.size(); j++)
			{
				if(naomi[k]<ken[j])
				{
					flag = true;
					ken.erase(ken.begin()+j);
					break;
				}
			}
			if(flag==false)
			{
				war++;
				ken.pop_back();
			}
		}
		
		for(int k=t-1; k>=0; k--)
		{
			bool flag = false;
			for(int j=0; j<dken.size(); j++)
			{
				if(dnao[k]>dken[j])
				{
					flag = true;
					break;
				}
			}
			if(flag==false)
			{
				dwar--;
				dken.erase(dken.begin());
			}
			else
				dken.pop_back();
		}
		cout<<"Case #"<<i<<": "<<dwar<<" "<<war<<endl;
	}
	return 0;
}