#include <iostream>
#include <vector>
#include <string>
using namespace std;

typedef long long LINT;

void main()
{
	int t;
	cin>>t;
	for(int ii=0; ii<t; ii++)
	{
		int n,m;
		cin>>n>>m;
		int pp[100]={0,};
		int cf=0;
		for(int i=0; i<m; i++)
		{
			int o,e,p;
			cin>>o>>e>>p;
			for(int j=o; j<e; j++)
			{
				pp[j]+=p;
				cf+=(n-(j-o))*p;
			}
		}

		int rf=0;
		for(int i=1; i<n; i++)
		{
			while(pp[i]>0)
			{
				for(int j=i; j<n; j++)
				{
					if(pp[j]==0)
						break;
					pp[j]--;
					rf+=n-(j-i);
				}
			}
		}

		cout<<"Case #"<<ii+1<<": "<<(cf-rf)%1000002013<<endl;
	}
}


