#include <cmath>
#include <cstdio>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>
#include <map>
#include <string>
using namespace std;


int getCount(string str,string digit)
{
	for(int i=0;i<str.size();i++)
	{
		
	}
}

int main()
{
	int t;	
	vector<string>input;
	cin>>t;
	for(int i = 0;i<t;i++)
	{
		string tmp;
		cin>>tmp;
		input.push_back(tmp);
		//cout<<tmp;
	}
	for(int i=0;i<t;i++)
	{
		long arr[10]={0};
		long countOfU = 0;
		long countofO = 0;
		long countOfS = 0;
		long countOfH = 0;
		long countOfF = 0;
		long countOfI = 0;
		for(int j=0;j<input[i].size();j++)
		{
			char curr = input[i][j];
			//cout<<curr<<endl;
			if(curr == 'Z')
			{
			arr[0]++;
			}
			else if(curr == 'U')
			{
			arr[4]++;
			countOfU++;
			}
			else if(curr == 'X')
			arr[6]++;
			else if(curr == 'G')
			arr[8]++;
			else if(curr == 'O')
			countofO++;
			else if(curr == 'S')
			countOfS++;
			else if(curr == 'H')
			countOfH++;
			else if(curr == 'W')
			arr[2]++;
			else if(curr == 'F')
			countOfF++;
			else if(curr == 'I')
			countOfI++;
			
		}
		arr[7] = countOfS - arr[6];
		arr[3] = countOfH - arr[8];
		arr[1] = countofO - arr[4]-arr[0]-arr[2];
		arr[5] = countOfF - arr[4];
		arr[9] = countOfI - arr[6]-arr[8]-arr[5];
		
		cout<<"Case #";
		cout<<i+1;
		cout<<": ";
		for(int k=0;k<10;k++)
		{
			for(int l=0;l<arr[k];l++)
			cout<<k;
		}
		cout<<endl;
	}
	
	
}

