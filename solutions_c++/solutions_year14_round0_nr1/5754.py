#include <iostream>
#include <cstring>

using namespace std;

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t;
	cin>>t;
	int id = 0;
	while(t--)
	{
		int r1,r2;
		cin>>r1;
		int a[5][5],b[5][5];
		bool f[18];
		memset(f,0,sizeof(f));
		for(int i = 0;i < 4;i++)
			for(int j = 0;j < 4;j++)
			{
				cin>>a[i][j];
				if(i == r1 - 1)
					f[a[i][j]] = 1;
			}
		cin>>r2;
		int fg = 0,re = -1;
		for(int i = 0;i < 4;i++)
			for(int j = 0;j < 4;j++)
			{
				cin>>b[i][j];
				if(i == r2 - 1)
				{
					if(f[b[i][j]] == 1)
					{
						fg++;
						re = b[i][j];
					}
				}
			}
		cout<<"Case #"<<++id<<": ";
		if(fg == 0)
			cout<<"Volunteer cheated!"<<endl;
		if(fg == 1)
			cout<<re<<endl;
		if(fg > 1)
			cout<<"Bad magician!"<<endl;
	}
	return 0;
}


