#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

void main()
{
	int t;
	cin>>t;
	cout<<t;
	for(int ii=0; ii<t; ii++)
	{
		int m,n; 
		vector<string> s;
		cin>>m>>n;
		for(int i=0; i<m; i++)
		{
			string ss;
			cin>>ss;
			s.push_back(ss);
		}
		
		int cnt=0;
		int maxn=-1;
		int nn=pow((double)n,m);
		for(int i=0; i<nn; i++)
		{
			int cc=i;
			vector<vector<string> > vs(n, vector<string>());
			for(int j=0; j<m; j++)
			{
				vs[cc%n].push_back(s[j]);
				cc/=n;
			}


			int nu=0;
			for(int j=0; j<vs.size(); j++)
			{
				for(int k=0; k<vs[j].size(); k++)
				{
					int mm=0;
					for(int l=0; l<k; l++)
					{
						int m=0;
						for(m=0; m<min(vs[j][k].length(), vs[j][l].length()); m++)
						{
							if(vs[j][l][m]!=vs[j][k][m])
								break;
						}
						mm=max(mm,m);
					}
					nu+=vs[j][k].length()-mm;
				}
				if(!vs[j].empty())
					nu++;
			}

			/*
			for(int j=0; j<vs.size(); j++)
			{
				for(int k=0; k<vs[j].size(); k++)
					cout<<vs[j][k]<<',';
				cout<<'/';
			}
			cout<<nu<<endl;
			*/

			if(nu>maxn)
			{
				cnt=1;
				maxn=nu;
			}
			else if(nu==maxn)
				cnt++;
		}	

		cout<<"Case #"<<ii+1<<": "<<maxn<<' '<<cnt<<endl;
	}
}
