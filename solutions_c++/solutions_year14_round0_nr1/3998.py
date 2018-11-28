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
	int cases;
	string line,temp;
	int oneAns,secAns;
	vector<int> first,second;
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small-attempt0.out","wt",stdout);
	cin>>cases;
	getline(cin,line);
	for (int x=0; x < cases ; x++)
	{
		first.clear();
		second.clear();
		cin>>oneAns;
		getline(cin,line);
		for (int i = 0; i < 4; i++)
		{
			getline(cin,line);
			istringstream strstr(line);
			if (i==oneAns-1)
			{
				for (int j = 0; j < 4; j++)
				{
					strstr >> temp;
					first.push_back(atoi(temp.c_str()));

				}
			}

		}

		cin>>secAns;
		getline(cin,line);
		for (int i = 0; i < 4; i++)
		{
			getline(cin,line);
			istringstream strstr(line);
			if (i==secAns-1)
			{
				for (int j = 0; j < 4; j++)
				{
					strstr >> temp;
					second.push_back(atoi(temp.c_str()));

				}
			}
		}
		int noFound=0;
		vector<int>::iterator num;
		for (int i = 0; i < 4; i++)
		{
			if(count(second.begin(),second.end(),first[i])==1)
			{
				num=find(second.begin(),second.end(),first[i]);
				noFound++;
			}
		}
		if (noFound<1)
		{
			cout<<"Case #"<<x+1<<": Volunteer cheated!"<<endl;
		}
		else if (noFound==1)
		{
			cout<<"Case #"<<x+1<<": "<<*num<<endl;
		}
		else if(noFound>1)
		{
			cout<<"Case #"<<x+1<<": Bad magician!"<<endl;
		}
	}
	return 0;

}

