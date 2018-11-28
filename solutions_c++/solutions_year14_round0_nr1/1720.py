// QualRound.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include "iostream"
#include "string"
#include "string.h"
#include "vector"
#include "algorithm"
using namespace std;

int main()
{
	freopen("A-small-attempt0.in.txt","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int T=0;
	cin>>T;
	for(int tc=0;tc<T;tc++)
	{
		int N;
		vector<int> g1,g2;
		cin>>N;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				int x;
				cin>>x;
				if(i==N-1)
					g1.push_back(x);
			}
		}
		cin>>N;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				int x;
				cin>>x;
				if(i==N-1)
					g2.push_back(x);
			}
		}
		int s=0;
		int chosen=-1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(g1[i]==g2[j])
				{
					chosen=g1[i];
					s++;
				}
			}
		}
		cout<<"Case #"<<tc+1<<": ";
		if(s==1)
		{
			cout<<chosen<<endl;
		}
		else if(s==0)
		{
			cout<<"Volunteer cheated!"<<endl;
		}
		else
		{
			cout<<"Bad magician!"<<endl;
		}
	}
	return 0;
}