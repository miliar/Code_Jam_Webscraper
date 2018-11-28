#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;
vector <double> naomi;
vector <double> ken;
int main() 
{
	int t,n;
	double x;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>x;
			naomi.push_back(x);
		}
		
		for(int i=0;i<n;i++)
		{
			cin>>x;
			ken.push_back(x);
		}
		
		sort(naomi.begin(),naomi.end());
		sort(ken.begin(),ken.end());
		int dw=0,w=0;
		vector <double> na=naomi;
		vector <double> ke=ken;
		// Start for deceitful war
		while(na.size()>0 && ke.size() >0)
		{
			if(na[0] > ke[ke.size()-1])
			{
				//cout<<"na[0] > ke[ke.size()-1]  na="<<na[0]<<" ke="<<ke[ke.size()-1]<<endl;
				dw+=na.size();
				break;
			}
			else
			{
				if(na[0] > ke[0])
				{
					//cout<<"na[0] > ke[0]  na="<<na[0]<<" ke="<<ke[0]<<endl;
					dw++;
					na.erase(na.begin()+0);
					ke.erase(ke.begin()+0);
				}
				else
				{
					//cout<<"na[0] < ke[0]  na="<<na[0]<<" ke="<<ke[0]<<endl;
					na.erase(na.begin()+0);
					ke.erase(ke.begin()+(ke.size()-1));
				}
			}
		}
		
		//End for deceitful war
		
		//Start for optimal war
		
		while(naomi.size() >0 && ken.size() > 0)
		{
			if(naomi[0] > ken[ken.size()-1])
			{
				//cout<<"na[0] > ke[ke.size()-1]  na="<<na[0]<<" ke="<<ke[ke.size()-1]<<endl;
				w+=naomi.size();
				break;
			}
			
			else
			{
				int i=0;
				while(i<ken.size() && naomi[0] > ken[i])
				{
					i++;
				}
				naomi.erase(naomi.begin()+0);
				ken.erase(ken.begin()+i);
			}
			
		}
		cout<<"Case #"<<k<<": "<<dw<<" "<<w<<endl;
		naomi.clear();
		ken.clear();
	}
	return 0;
}