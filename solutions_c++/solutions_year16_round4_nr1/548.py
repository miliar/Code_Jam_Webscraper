// Round2.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include "iostream"
#include "vector"
#include "algorithm"
#include "string"
using namespace std;

string ans[15][5];

int main()
{
	//freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	ans[0][1]="P";
	ans[0][2]="R";
	ans[0][3]="S";
	for(int n=1;n<=12;n++)
	{
		ans[n][1]=min(ans[n-1][1]+ans[n-1][2], ans[n-1][2]+ans[n-1][1]);
		ans[n][2]=min(ans[n-1][2]+ans[n-1][3], ans[n-1][3]+ans[n-1][2]);
		ans[n][3]=min(ans[n-1][1]+ans[n-1][3], ans[n-1][3]+ans[n-1][1]);
	}
	for(int tc=0;tc<T;tc++)
	{
		int N,R,P,S;
		cin>>N>>R>>P>>S;
		string output;
		for(int i=1;i<=3;i++)
		{
			int cr=0,cp=0,cs=0;
			for(int j=0;j<ans[N][i].size();j++)
			{
				if(ans[N][i][j]=='R') cr++;
				if(ans[N][i][j]=='P') cp++;
				if(ans[N][i][j]=='S') cs++;
			}
			if(cr==R && cp==P && cs==S)
			{
				if(output.size()==0)
				{
					output=ans[N][i];
				}
				else
				{
					output=min(ans[N][i],output);
				}
			}
		}
		if(output.size()==0)
		{
			cout<<"Case #"<<tc+1<<": IMPOSSIBLE"<<endl;
		}
		else
		{
			cout<<"Case #"<<tc+1<<": "<<output<<endl;
		}
	}
	return 0;
}

