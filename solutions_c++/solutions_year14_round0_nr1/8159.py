#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>
#include <set>
#include <stack>
#include <list>
#include <fstream>

using namespace std;

int main()
{
	std::ios_base::sync_with_stdio(false);

	int t,ans1,ans2,grid1[4][4],grid2[4][4],flag=0,ans[4],single_ans;
	ofstream output;
    output.open("output.txt");
	ifstream input;
	input.open("input.txt");
	input>>t;

	for(int index=1;index<=t;index++)
	{
		flag=0;

		input>>ans1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				input>>grid1[i][j];

		input>>ans2;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				input>>grid2[i][j];

		for(int j=0;j<4;j++)
			ans[j]=grid1[ans1-1][j];

		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(grid2[ans2-1][i]==ans[j])
				{
					if(flag==0)
					{
						flag=1;
						single_ans=ans[j];
					}else{
						flag=2;
						break;
					}
				}
			}
			if(flag==2)
				break;
		}

		if(flag==0)
			output<<"case #"<<index<<": Volunteer cheated!"<<endl;
		else if(flag==1)
			output<<"case #"<<index<<": "<<single_ans<<endl;
		else
			output<<"case #"<<index<<": Bad magician!"<<endl;

	}
	output.close();
	input.close();

	return 0;
}
