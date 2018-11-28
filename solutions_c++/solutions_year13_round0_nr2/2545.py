/*
ID: amin_un1
PROG: ride
LANG: C++
*/

/*
my ID
uva = "sir sbu"
codforsec = "sirsbu"
topcoder = "sir_sbu"
usaco = "amin_un1"
*/
#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <queue>
#include <cmath>
#include <sstream>
#include <fstream>
#include <string.h>
#include <string>
#include <map>
#include <stack>
#include <set>
#define LL long long
#define Endl endl
#define all(n) (n).begin(), (n).end()
using namespace std;
const LL mod=1000*1000*1000+7LL;
const double EXP = 1e-6;
const int MAX = 100001;

int main()
{
	//ofstream cout ("test.out");
    //ifstream cin ("test.in");
    //freopen("output.txt", "w", stdout);
    //freopen("input.txt", "a", stdout);
    int tc;
    cin>>tc;
    int t=0;
    while(tc--)
    {
		t++;
		int n,m;
		cin>>n>>m;
		int a[101][101];
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				cin>>a[i][j];
			}
		}
		bool mark[101][101];
		memset(mark,0,sizeof mark);
		bool b=0;
		for(int i=0;i<n;i++)
		{
			int ma=0;
			for(int j=0;j<m;j++)
			ma=max(ma,a[i][j]);
			for(int j=0;j<m;j++)
			{
				if(a[i][j]!=ma)
				{
					int maa=0;
					for(int k=0;k<n;k++)
					maa=max(maa,a[k][j]);
					if(maa!=a[i][j])
					{
						b=1;i=n;j=m;
					}
				}
			}
		}
		if(!b)
		cout<<"Case #"<<t<<": YES"<<endl;
		else
		cout<<"Case #"<<t<<": NO"<<Endl;
	}
	return 0;
}


