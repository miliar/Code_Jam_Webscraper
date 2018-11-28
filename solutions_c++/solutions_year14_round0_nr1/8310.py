#include <fstream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>
#include <cmath>
using namespace std;

ifstream cin("A-small-attempt0.in");
ofstream cout("output2.txt");

int main()
{

	int t,i,j;

	int a[10][10], b[10][10];

	int x, y;

	cin>>t;

	for(int l=0; l<t; ++l)
	{
		cin>>x;
		for(i=1; i<=4; ++i)
			for(j=1; j<=4; ++j)
				cin>>a[i][j];

		cin>>y;
		for(i=1; i<=4; ++i)
			for(j=1; j<=4; ++j)
				cin>>b[i][j];

		int k = 0;
		int res;

		for(i=1; i<=4; ++i)
		{
			for(j=1; j<=4; ++j)
				if(a[x][i]==b[y][j])
				{
					++k;
					res = a[x][i];
				}

		}
		cout<<"Case #"<<l+1<<": ";
		if(k==1)
			cout<<res<<endl;
		if(k==0)
			cout<<"Volunteer cheated!"<<endl;
		if(k>1)
			cout<<"Bad magician!"<<endl;
	}

	return 0;
}