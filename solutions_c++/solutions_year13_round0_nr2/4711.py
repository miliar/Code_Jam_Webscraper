#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <ctime>
#include <math.h>
#include <vector>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <sstream>
#include <complex>
using namespace std;


#define X first
#define Y second
#define pb push_back
#define mp make_pair

const double PI = acos(-1.0);
const double INF = 1000000000;
const int MOD = 1073741824;
const int M = INF;
const double RRR = 180.0/PI;


typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector<int> vi;



int main()
{
	//#ifndef ONLINE_JUDGE
	freopen("INPUT.TXT","r",stdin);
	freopen("OUTPUT.TXT","w",stdout);
	//#endif
	int t;
	cin>>t;
	for(int test=1; test<=t; test++)
	{
		int n,m;
		cin>>n>>m;
		vector<vector<int> > mas(n,vector<int>(m)), ans(n,vector<int>(m,100));
		for(int i=0; i<n; i++)
		{
			for(int j=0; j<m; j++)
			{
				cin>>mas[i][j];
			}
		}
		for(int i=0; i<n; i++)
		{
			int y=mas[i][0];
			for(int j=0; j<m; j++)
			{
				if(mas[i][j]>y)
				{
					y=mas[i][j];
				}
			}
			for(int j=0; j<m; j++)
			{
				ans[i][j]=y;
			}
		}
		for(int j=0; j<m; j++)
		{
			int y=mas[0][j];
			for(int i=0; i<n; i++)
			{
				if(mas[i][j]>y)
				{
					y=mas[i][j];
				}
			}
			for(int i=0; i<n; i++)
			{
				if(ans[i][j]>y)
				{
					ans[i][j]=y;
				}
			}
		}
		for(int i=0; i<n; i++)
		{
			for(int j=0; j<m; j++)
			{
				if(mas[i][j]!=ans[i][j])
				{
					cout<<"Case #"<<test<<": NO"<<endl;
					goto end;
				}
			}
		}
		cout<<"Case #"<<test<<": YES"<<endl;
		end:;
	}
	return 0;
}