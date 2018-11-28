#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;
int t, kol, k;
bool ok[22];
int main()
{
	//ifstream cin("input.txt");
	//ofstream cout("output.txt");
	cin>>t;
	for(int kol=1;kol<=t;kol++)
	{
		for(int i=1;i<17;++i)
			ok[i]=true;
		int x;
		cin>>x;
		for(int i=1; i<=4; ++i)
			for(int j=1; j<=4; ++j)
			{
				int y;
				cin>>y;
				if (i!=x)
					ok[y]=false;
			}
		cin>>x;
		for(int i=1; i<=4; ++i)
			for(int j=1; j<=4; ++j)
			{
				int y;
				cin>>y;
				if (i!=x)
					ok[y]=false;
			}
		k=0;
		for(int i=1;i<=16;++i)
			k+=ok[i];
		cout<<"Case #"<<kol<<": ";
		if (k==0)
		{
			cout<<"Volunteer cheated!\n";
			continue;
		}
		if (k==1)
		{
			for(int i=1;i<=16;++i)
				if (ok[i])
					cout<<i<<"\n";
			continue;
		}
		cout<<"Bad magician!\n";
	}
	return 0;
}