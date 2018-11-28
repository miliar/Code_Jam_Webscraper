#include <iostream>
#include <sstream>
#include <fstream>
#include <stdio.h>
#include <numeric>
#include <vector>
#include <string>
#include <math.h>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <string.h>
#include <tuple> 
#include <iomanip>
using namespace std;


void ReadArrang(vector<vector<int>> & V)
{
	int temp;
	for (int j = 0; j < 4; j++)
	{
		vector<int> row;
		for (int k = 0; k < 4; k++)
		{
				cin>>temp;
				row.push_back(temp);
		}
		V.push_back(row);
	}
}
int GetAns(const vector<vector<int>> & V1,const vector<vector<int>> & V2,int R1, int R2)
{
	int count = 0;//
	int common = -1;
	for (int i = 0; i < V1[R1].size(); i++)
	{
		for (int j = 0; j < V2[R2].size(); j++)
		{
			if (V1[R1][i] == V2[R2][j])
			{
				common = V1[R1][i];
				count++;
			}
		}
	}

	if (count == 0)
	{
		return -1;//cheated
	}
	if (count == 1)
	{
		return common;
	}
	return -2;//bad
}
int main(int argc, const char **argv) 
{	
	freopen("A-small-attempt0.in","r",stdin);
	freopen("Magic Trick.out","w",stdout);
	int R1, R2,temp;
	vector<vector<int>> V1, V2;
	int T;
	cin>>T;
	for (int i = 0; i < T; i++)
	{
		vector<vector<int>> V1, V2;
		cin>>R1;
		R1--;
		ReadArrang(V1);
		cin>>R2;
		R2--;
		ReadArrang(V2);
		int ans = GetAns(V1,V2,R1,R2);
		if (ans == -1)
		{
			cout<<"Volunteer cheated!\n";

		}else if (ans == -2)
		{
			cout<<"Bad magician!\n";
		}
		else
		{
			cout<<ans<<endl;
		}
	}

	return 0;
}