#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <queue>

using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int N=0; N<T; N++)
	{
		int a1, a2;
		int grid[4][4], row[4];
		vector<int> answers;
		cin>>a1;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				cin>>grid[i][j];
		for(int i=0; i<4; i++)
			row[i]=grid[a1-1][i];
		cin>>a2;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				cin>>grid[i][j];
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
				if(grid[a2-1][i]==row[j])
					answers.push_back(row[j]);
		}
		if(answers.size()==1)
			cout<<"Case #"<<N+1<<": "<<answers[0]<<endl;
		else if(answers.size()==0)
			cout<<"Case #"<<N+1<<": Volunteer cheated!"<<endl;
		else
			cout<<"Case #"<<N+1<<": Bad magician!"<<endl;
	}
	return 0;
}