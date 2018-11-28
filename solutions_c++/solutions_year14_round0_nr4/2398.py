#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int decWar(vector<double> naomi, vector<double> ken, int n)
{
	int i,j;
	bool c;
	
	i=0;
	
	while(1)
	{
		c=true;
		if(naomi[i]>ken[i])
		{
			i++;
		}
		else
		{
			naomi.erase(naomi.begin());
			ken.pop_back();
			i=0;
			n--;
			c=false;
		}
		if(i==n) break;
	}
	
	return n;
}

int norWar(vector<double> naomi, vector<double> ken, int n)
{
	int i,j;
	bool c;
	
	for(i=0;i<n;i++)
	{
		c=false;
		
		for(j=0;j<n;j++)
		{
			if(ken[j]>naomi[i])
			{
				naomi.erase(naomi.begin()+i);
				ken.erase(ken.begin()+j);
				j--;
				i--;
				n--;
				c=true;
				break;
			}
		}
		if(c==false) break;
	}
	
	return n;
}

int main()
{
	int test,i,n,j;
	double x;
	vector<double> naomi1,ken1,naomi2,ken2;
	i=0;
	cin>>test;
	while(test>i)
	{
		cin>>n;
		for(j=0;j<n;j++)
		{
			cin>>x;
			naomi1.push_back(x);
		}
		sort(naomi1.begin(),naomi1.end());
		naomi2=naomi1;
		
		for(j=0;j<n;j++)
		{
			cin>>x;
			ken1.push_back(x);
		}
		sort(ken1.begin(),ken1.end());
		ken2=ken1;
		i++;
		cout<<"Case #"<<i<<": ";
		cout<<decWar(naomi1,ken1,n)<<" ";
		cout<<norWar(naomi2,ken2,n)<<endl;
		ken1.clear();
		ken2.clear();
		naomi1.clear();
		naomi2.clear();
		
	}
}
