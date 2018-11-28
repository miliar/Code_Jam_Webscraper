#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct box { char x; int c;};
vector< struct box > v[200];

int main()
{
	int tc;
	cin>>tc;
	int cno = 1;
	while(tc--)
	{
		int n;
		cin>>n;
		for(int i=0;i<n;i++)
		{
			string s;
			cin>>s;
			struct box bx;
			bx.x = s[0];
			bx.c = 1;
			for(int j=1;j<s.length();j++)
			{
				if(s[j] == bx.x)
				{
					bx.c++;
				}
				else
				{
					v[i].push_back(bx);
					bx.x = s[j];
					bx.c = 1;
				}
			}
			v[i].push_back(bx);
		}

		

		int f = 0;
		for(int i=0;i<n-1;i++)
			if(v[i].size() != v[i+1].size())
			{
				f = 1;
				break;
			}

		int changes = 0,poss = 0;
		if(f == 0)
		{
			for(int j=0;j<v[0].size();j++)
			{
				int count = v[0][j].c;
				int ff = 0;
				for(int i=1;i<n;i++)
				{
					if(v[i][j].x != v[i-1][j].x)
					{
						ff = 1;
						break;
					}
					else
						count += v[i][j].c;
				}

				if(ff == 0)
				{
					int final = count / n;
					for(int i=0;i<n;i++)
						changes += abs(v[i][j].c - final);
					poss = 1;
				}
				else
				{
					poss = 0;
					break;
				}
			}
			if(poss == 1)
			{
				cout<<"Case #"<<cno<<": "<<changes<<endl;
			}
			else
			{
				cout<<"Case #"<<cno<<": Fegla Won"<<endl;
			}
		}
		else
		{
			poss = 0;
			cout<<"Case #"<<cno<<": Fegla Won"<<endl;
		}

		for(int i=0;i<200;i++)
			v[i].clear();
		cno++;
	}
}