#include <iostream>
#include <vector>

using namespace std;

int main()
{
	string s;
	int t;
	cin>>t;
	char v[]={'O','X'};
	for(int z=0;z<t;z++)
	{
		getline(cin,s);
		vector<string> grid(4);
		for(int i=0;i<4;i++)
		{
			getline(cin,s);
			grid[i]=s;
		}
		bool ended=true;
		cout<<"Case #"<<z+1<<": ";
		for(int i=0;i<2;i++)
		{
			char c=v[i];
			for(int j=0;j<4;j++)
			{
				bool ok1=true;
				bool ok2=true;
				for(int k=0;k<4;k++)
				{
					if(grid[j][k]=='.'||grid[k][j]=='.')
					{
						ended=false;
					}
					if(grid[j][k]!='T'&&grid[j][k]!=c)
					{
						ok1=false;
					}
					if(grid[k][j]!='T'&&grid[k][j]!=c)
					{
						ok2=false;
					}					
				}	
				if(ok1||ok2)
				{
				cout<<c<<" won\n";
				goto end;
				}			
			}
			bool ok1=true,ok2=true;
			for(int j=0;j<4;j++)
			{
				if(grid[j][j]!='T'&&grid[j][j]!=c)
				{
					ok1=false;
				}
				if(grid[j][3-j]!='T'&&grid[j][3-j]!=c)
				{
					ok2=false;
				}
			}
			if(ok1||ok2)
			{
				cout<<c<<" won\n";
				goto end;
			}
		}
		if(ended)
		{
			cout<<"Draw\n";
		}
		else
		{
			cout<<"Game has not completed\n";
		}
		end:;
	}
	cout<<flush;
}
