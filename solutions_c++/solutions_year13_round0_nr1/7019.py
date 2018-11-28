//Solution by Daniyar Maminov                                                                                                                                                                     
#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<math.h>
#include<vector>
#include<cstring>
#include<queue>
#include<map>
#include<set>
#define mp make_pair
#define f first
#define pb push_back
#define s second
#define ub upper_bound
#define lb lower_bound
#define inf 1000*1000*1000
using namespace std;

char c[5][5], ch;

int n, i, j, m, k, l, k1;

string ans[13];

bool found;

int main()
{
//	#ifndef ONLINE_JUDGE
	freopen (".in","r",stdin);
	freopen (".out","w",stdout);
//	#endif
	cin>>n;
	ans[1]="X won";
	ans[2]="O won";
	ans[3]="Draw";
	ans[4]="Game has not completed";
	for (int cs=1; cs<=n; cs++)
	{
		found=0;
		cout<<"Case #"<<cs<<": ";
		for (i=1; i<=4; i++)
		{
			for (j=1; j<=4; j++)
			{
				cin>>c[i][j];
			}
		}
		for (i=1; i<=4; i++)
		{
			k=0, k1=0;
			for (j=1; j<=4; j++)
			{
				if (c[i][j]=='T')
					k++, k1++;
				if (c[i][j]=='X')
					k++;
				if (c[i][j]=='O')
					k1++;
			}
			if (k==4)
			{
				cout<<ans[1]<<endl;
				found=1;
				break;
			}
			if (k1==4)
			{
				cout<<ans[2]<<endl;
				found=1;
				break;
			}
	   	}
	   	if (found) continue;
		for (i=1; i<=4; i++)
		{
			k=0, k1=0;
			for (j=1; j<=4; j++)
			{
				if (c[j][i]=='T')
					k++, k1++;
				if (c[j][i]=='X')
					k++;
				if (c[j][i]=='O')
					k1++;
			}
			if (k==4)
			{
				cout<<ans[1]<<endl;
				found=1;
				break;
			}
			if (k1==4)
			{
				cout<<ans[2]<<endl;
				found=1;
				break;
			}
	   	}
	   	if (found) continue;
		k=0, k1=0;
		for (j=1; j<=4; j++)
		{
			if (c[j][j]=='T')
				k++, k1++;
			if (c[j][j]=='X')
				k++;
			if (c[j][j]=='O')
				k1++;
		}
		if (k==4)
		{
			cout<<ans[1]<<endl;
			continue;
		}
		if (k1==4)
		{
			cout<<ans[2]<<endl;
			continue;
		}
		k=0, k1=0;
		for (j=1; j<=4; j++)
		{
			if (c[j][4-j+1]=='T')
				k++, k1++;
			if (c[j][4-j+1]=='X')
				k++;
			if (c[j][4-j+1]=='O')
				k1++;
		}
		if (k==4)
		{
			cout<<ans[1]<<endl;
			continue;
		}
		if (k1==4)
		{
			cout<<ans[2]<<endl;
			continue;
		}
		for (i=1; i<=4; i++)
		{
			for (j=1; j<=4; j++)
			{
				if (c[i][j]=='.')
				{
					cout<<ans[4]<<endl;
					found=1;
					break;
				}
			}
			if (found) break;
		}
		if (found) continue;
		cout<<ans[3]<<endl;
	}
	  
	   		
	   	


	return 0;
}