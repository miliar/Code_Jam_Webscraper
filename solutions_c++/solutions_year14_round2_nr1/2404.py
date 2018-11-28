#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <math.h>
#include <stdlib.h>
using namespace std;

vector<vector<pair<char,int> > > input;
vector<int> ans;
int main()
{
	ifstream in("A-small-attempt0.in");
	ofstream out("out.txt");
	int k;
	in>>k;
	ans.resize(k);
	for(int z = 0;z<k;z++)
	{
		int n;
		in>>n;
		input.clear();
		input.resize(n);
		for(int i=0;i<n;i++)
		{
			string temp;
			in>>temp;
			int count = 0;
			for(int j=0;j<temp.size();j++)
			{
				if(!count || temp[j]==temp[j-1])
				{
					count++;
				}
				else
				{
					j--;
					input[i].push_back(make_pair(temp[j],count));
					count = 0;
				}
			}
			if(count)
			{
				input[i].push_back(make_pair(temp[temp.size()-1],count));
			}
		}
		int equal = input[0].size();
		bool canDo = true;
		for(int j = 1;j < n;j++)
		{
			if(input[j].size() != equal)
			{
				canDo = false;
				ans[z] = -1;
				break;
			}
		}

		if(canDo)
		for(int i =0;i<input[0].size();i++)
		{
			int sum = 0;
			if(canDo)
			for(int j = 0;j<n;j++)
			{
				if(input[j][i].first != input[0][i].first)
				{
					canDo = false;
					break;
				}
				else
				{
					sum += input[j][i].second;
				}
			}
			else
			{
				ans[z] = -1;
				break;
			}
			
			if(canDo)
			{
				int sum1=0, sum2=0;
				for(int j = 0;j<n;j++)
				{
					sum1 += abs(sum/n - input[j][i].second);
					sum2 += abs(sum/n + 1 - input[j][i].second);
				}
				ans[z] += min(sum1,sum2);
			}
			else
			{
				ans[z] = -1;
				break;
			}

		}
	}
	for(int i = 0;i<k;i++)
	{
		if(ans[i]>=0)
			out<<"Case #"<<i+1<<": "<<ans[i]<<endl;
		else
		{
			out<<"Case #"<<i+1<<": Fegla Won"<<endl;
		}
	}
	return 0;
}