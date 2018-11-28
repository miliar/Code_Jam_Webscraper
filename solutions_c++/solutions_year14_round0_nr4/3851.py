#include <iostream>
#include <fstream>
#define _USE_MATH_DEFINES
#include <math.h>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <functional>
#include <string>
#include <cstring>

using namespace std;

int main()
{
	int cases,N;
	string line,temp;
	vector<double> naomi,naomi1,ken,ken1;
	vector<double>::iterator minNaomi;
	freopen("D-large.in","rt",stdin);
	freopen("D-large.out","wt",stdout);
	cin>>cases;
	getline(cin,line);
	for (int i=0; i < cases ; i++)
	{
		naomi.clear();
		ken.clear();
		N=0;
		cin>>N;
		getline(cin,line);
		getline(cin,line);
		istringstream strstr(line);
		while (strstr >> temp)
		{
			naomi.push_back(atof(temp.c_str()));
		}

		getline(cin,line);
		istringstream strstr2(line);
		while (strstr2 >> temp)
		{
			ken.push_back(atof(temp.c_str()));
		}
		naomi1=naomi;
		ken1=ken;
		int win=N,dWin=0;
		sort(naomi.begin(),naomi.end());
		sort(ken.begin(),ken.end());
		while(naomi.size()>0)
		{
			double firstMax=naomi[0];
			int maxIndex=-1;
			for (int a = 0;  a < ken.size();  a++)
			{
				if (ken[a]>firstMax)
				{
					firstMax=ken[a];
					maxIndex=a;
					break;
				}
				
			}
			if(maxIndex>=0)
			{
				ken.erase(ken.begin()+maxIndex);
				win--;
				naomi.erase(naomi.begin());
			}
			else
			{
				break;
			}

		}
		naomi=naomi1;
		ken=ken1;
		sort(naomi.begin(),naomi.end());
		sort(ken.rbegin(),ken.rend());
		while (ken.size()>0)
		{
			double firstMax=ken[0];
			int maxIndex=-1;
			for (int a = 0;  a < naomi.size();  a++)
			{
				if (naomi[a]>firstMax)
				{
					firstMax=naomi[a];
					maxIndex=a;
					break;
				}
			}
			if(maxIndex>=0)
			{
				ken.erase(ken.begin());
				dWin++;
				naomi.erase(naomi.begin()+maxIndex);
			}
			else
			{
				ken.erase(ken.begin());
				naomi.erase(naomi.begin());
			}
		}
		cout<<"Case #"<<i+1<<": "<<dWin<<" "<<win<<endl;
	}
	return 0;

}