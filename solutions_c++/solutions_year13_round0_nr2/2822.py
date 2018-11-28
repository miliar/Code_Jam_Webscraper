#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>

using namespace std;

#define pb push_back
#define all(x) (x).begin(), (x).end()
#define mk make_pair

int a[105][105];
int n,m;

bool check_line(int i, int h)
{
	for(int j = 0; j < m; j++)
		if( a[i][j] > h ) return false;
	return true;
}

bool check_raw(int j, int h)
{
	for(int i = 0; i < n; i++)
		if( a[i][j] > h ) return false;
	return true;
}

bool solve()
{
	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < m; j++)
			scanf("%d",&a[i][j]);
	}
	
	//vert
	for(int j = 0; j < m; j++)
	{
		bool b = false;
		for(int i = 0; i < n; i++)
			if( !( i == 0 || a[i-1][j] == a[i][j]) ) b = true;
		//if not all hights are equal
		if( b )
		{
			//check horizaontal lines
			for(int i = 0; i < n; i++)
				if( !check_line(i, a[i][j]) ) return false;
		}
	}
	
	for(int i = 0; i < n; i++)
	{
		bool b = true;
		for(int j = 0; j < m; j++)
			if( !( j == 0 || a[i][j] == a[i][j-1] ) ) b = false;
		if( !b )
		{
			for(int j = 0; j < m; j++)
				if( !check_raw(j, a[i][j]) ) return false;
		}
	}
	return true;
}

int main()
{	
	freopen("B-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	
	for(int i = 0; i < t; i++)
	{	
		cin >> n >> m;
		printf("Case #%d: %s\n",i+1, solve()?"YES":"NO");
	}
	
	return 0;
}
