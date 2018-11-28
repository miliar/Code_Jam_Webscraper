#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <map>
#include <list>
#include <algorithm>
#include <functional>
#include <unordered_map>
//#include <tr1/thread>
using namespace std;

#define NUM 4
char b[NUM][NUM];

void Solve(int nCase)
{
	int rowCount[2][NUM]={0};//0:x,1:y
	int colCount[2][NUM]={0};
	int diaCount[2][2]={0};
	int dotCnt = 0;
	for(int i=0;i<NUM;i++)
	{
		for(int j=0;j<NUM;j++)
		{
			if(b[i][j] == 'X')
			{
				rowCount[0][i]++;
				colCount[0][j]++;
				if(i == j)
					diaCount[0][0]++;
				else if(i+j == NUM-1)
					diaCount[0][1]++;
			}
			else if(b[i][j] == 'O')
			{
				rowCount[1][i]++;
				colCount[1][j]++;
				if(i == j)
					diaCount[1][0]++;
				else if(i+j == NUM-1)
					diaCount[1][1]++;
			}
			else if(b[i][j] == 'T')
			{
				rowCount[0][i]++;
				colCount[0][j]++;
				rowCount[1][i]++;
				colCount[1][j]++;
				if(i == j)
				{
					diaCount[0][0]++;
					diaCount[1][0]++;
				}
				else if(i+j == NUM-1)
				{
					diaCount[0][1]++;
					diaCount[1][1]++;
				}
			}
			else
				dotCnt++;
		}
	}
	//check 
	for(int i=0;i<NUM;i++)
	{
		if(rowCount[0][i] == 4)
		{
			cout<<"Case #"<<nCase<<": X won"<<endl;
			return;
		}
		else if(rowCount[1][i] == 4)
		{

			cout<<"Case #"<<nCase<<": O won"<<endl;
			return;	
		}
		if(colCount[0][i] == 4)
		{
			cout<<"Case #"<<nCase<<": X won"<<endl;
			return;	
		}
		else if(colCount[1][i] == 4)
		{

			cout<<"Case #"<<nCase<<": O won"<<endl;
			return;	
		}
	}
	for(int i=0;i<2;i++)
	{
		if(diaCount[0][i] == 4)
		{
			cout<<"Case #"<<nCase<<": X won"<<endl;
			return;
		}
		if(diaCount[1][i] == 4)
		{
			cout<<"Case #"<<nCase<<": O won"<<endl;
			return;
		}
	}
	if(dotCnt == 0)
	{
			cout<<"Case #"<<nCase<<": Draw"<<endl;
			return;
	}
	cout<<"Case #"<<nCase<<": Game has not completed"<<endl;

}
int main(int argc, char const *argv[])
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>b[i][j];
		Solve(t);
	}
	return 0;
}