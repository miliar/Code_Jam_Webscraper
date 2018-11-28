#include <iostream>
# include <string>
# include <map>
# include <stdio.h>
using namespace std;
int main()
{
	freopen("CODEJAM_Q1.txt","w",stdout);
	int t;
	cin>>t;
	for (int tc=1;tc<=t;tc++)
	{
		int first=-1;
		int c=0;
		map<int,int> m;
		int r1;
		cin>>r1;
		for (int i=0;i<4;i++)
		{
			for (int x=0;x<4;x++)
			{
				int y;
				cin>>y;
				if (i==r1-1)
				{
					m[y]++;
				}
			}
		}
		int r2;
		cin>>r2;
		for (int i=0;i<4;i++)
		{
			for (int x=0;x<4;x++)
			{
				int y;
				cin>>y;
				if (i==r2-1)
				{
					m[y]++;
					if (m[y]==2)
						c++;
					if (c==1 && first==-1)
						first=y;
				}
			}
		}
		cout<<"Case #"<<tc<<": ";
		if (c==1)
			cout<<first<<endl;
		else if (c==0)
			cout<<"Volunteer cheated!"<<endl;
		else
			cout<<"Bad magician!"<<endl;
	}
}