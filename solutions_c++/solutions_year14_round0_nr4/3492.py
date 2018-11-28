#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() 
{
	int zc;
	cin>>zc;
	for(int tc=1;tc<=zc;tc++)
	{
		int n, nptn=0, nptk=0,dptn=0,dptk=0;
	       	vector<float> naomi, ken;

		cin>>n;
		for(int i=0;i<n;i++)
		{
			float tmp;
			cin>>tmp;
			naomi.push_back(tmp);
		}
		for(int i=0;i<n;i++)
		{
			float tmp;
			cin>>tmp;
			ken.push_back(tmp);
		}
		sort(naomi.begin(),naomi.end());
		sort(ken.begin(),ken.end());
		vector<float> ken2( ken);
		//Normal war
		int i=0,j=0,k=0;
		while(i<n||j<ken2.size())
		{
			if(naomi[i]>ken2[j])
			{
				int flag=1;
				for(;k<ken2.size();k++)
					if(ken2[k]>naomi[i])
					{
						nptk++;
						i++;
						ken2.erase(ken2.begin()+k);
						flag=0;
						k--;
						break;
					}
				if(flag)
				{
					nptn++;
					i++;
					j++;
				}
			}
			else 
			{
				nptk++;
				i++;
				j++;
			}
		}
		//Deceitful war
		i=0;
		j=0;
		k=n-1;
		while(i<n||j<=k)
		{
			if(naomi[i]>ken[j])
			{
				dptn++;
				i++;
				j++;
			}
			else if(naomi[i]<ken[k])
			{
				dptk++;
				i++;
				k--;
			}
		}
		cout<<"Case #"<<tc<<": "<<dptn<<' '<<nptn<<endl;
	}
}
