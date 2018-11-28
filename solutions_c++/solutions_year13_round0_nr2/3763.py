#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	int z; cin>>z; for(int ii=0; ii<z; ii++)
	{
		bool tab[101][101];
		int t[101][101];
		int n; int m; cin>>n>>m;
		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++)
			tab[i][j]=false;
		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++)
			cin>>t[i][j];
		for(int i=0; i<n; i++)
		{
			int maxx=-1;
			for(int j=0; j<m; j++)
			{
				maxx=max(maxx, t[i][j]);
			}
			for(int j=0; j<m; j++)
			{
				if(t[i][j]==maxx)
				tab[i][j]=true;
			}
		}
		for(int j=0; j<m; j++)
		{
			int maxx=-1;
			for(int i=0; i<n; i++)
			{
				maxx=max(maxx, t[i][j]);
			}
			for(int i=0; i<n; i++)
			{
				if(t[i][j]==maxx)
				tab[i][j]=true;
			}
		}
		bool k=true;
		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++)
			if(!tab[i][j])
			k=0;
		if(k)
		cout<<"Case #"<<ii+1<<": YES";
		else
		cout<<"Case #"<<ii+1<<": NO";
		
		cout<<endl;
	}
	return 0;
}
