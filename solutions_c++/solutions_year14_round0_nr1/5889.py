#include <iostream>
#include <limits.h>
#include <string.h>
#include <queue>
#include <stdio.h>
#include <vector> 
#include <algorithm> 
#include <cmath>
#include <unistd.h>
#include <map>
#include <set>
using namespace std;
typedef pair<int,int> PII;

int main()
{
	int t;
	cin >> t;
	int tc = 0;
	vector<vector<int> > r1(4);
	vector<vector<int> > r2(4);
		//r1.resize(4);
		for(int i = 0; i < 4; i++)
		{
			r1[i].resize(4);
			r2[i].resize(4);
		}
			
	while(t--)
	{
		int rowguess1, rowguess2;
		cin >> rowguess1;
		
		
		for(int x = 0; x < 4; x++)
		{
			for(int y = 0; y < 4; y++)
			{
				cin >> r1[x][y];
			}
		}
		
		cin >> rowguess2;
		
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				cin >> r2[i][j];
			}
		}
		
		//for(int j = 0; j < 4; j++)
		//{
				//cout << r1[rowguess1-1][j] << " ";
			//}
		//for(int j = 0; j < 4; j++)
		//{
				//cout << r2[rowguess2-1][j] << " ";
			//}
		
		vector<int> aux1(r1[rowguess1-1].begin(), r1[rowguess1-1].end());
		vector<int> aux2(r2[rowguess2-1].begin(), r2[rowguess2-1].end());
		sort(aux1.begin(), aux1.end());
		sort(aux2.begin(), aux2.end());
		
		vector<int> ans(aux1.size()+aux2.size());
		vector<int>::iterator iter;
		iter = set_intersection (aux1.begin(),aux1.end(),aux2.begin(),aux2.end(), ans.begin());
		ans.resize(iter-ans.begin());
		if(ans.size()==0)
			cout <<"Case #"<<tc+1<<": "<< "Volunteer cheated!" << endl;
		else if(ans.size()==1)
			cout <<"Case #"<<tc+1<<": "<<ans[0] << endl;
		else
			cout <<"Case #"<<tc+1<<": "<<"Bad magician!" << endl;
	  tc++;
	}
			
	return 0;
}
