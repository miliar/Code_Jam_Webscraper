#ifdef _WIN32
#define _CRT_SECURE_NO_DEPRECATE
#endif

//#include "stdafx.h"
//#include <conio.h>

#include <iostream>
#include <fstream>

#include <stdio.h>
#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <math.h>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>

//#pragma comment (linker, "/STACK:10000000000000")
#define pi 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998


using namespace std;

int solve(vector <string> v)
{
	bool d=0;
	bool o=0;
	bool x=0;

	for (int i=0; i<4; i++)
	{
		int couX=0;
		int couO=0;
		int couD=0;
		bool t=0;


		for (int j=0; j<4; j++)
		{
			if (v[i][j]=='X')
			{
				couX++;
				continue;
			}
			if (v[i][j]=='O')
			{
				couO++;
				continue;
			}
			if (v[i][j]=='.')
			{
				couD++;
				continue;
			}
			if (v[i][j]=='T')
			{
				t=1;
				continue;
			}
		}
		if ((couX==4)||(couX==3 && t))
		{
			x=1;
			break;
		}
		if ((couO==4)||(couO==3 && t))
		{
			o=1;
			break;
		}
		if (couD)
			d=1;
	}

	if (x)
		return 1;
	if (o)
		return 2;

	for (int j=0; j<4; j++)
	{
		int couX=0;
		int couO=0;
		int couD=0;
		bool t=0;


		for (int i=0; i<4; i++)
		{
			if (v[i][j]=='X')
			{
				couX++;
				continue;
			}
			if (v[i][j]=='O')
			{
				couO++;
				continue;
			}
			if (v[i][j]=='.')
			{
				couD++;
				continue;
			}
			if (v[i][j]=='T')
			{
				t=1;
				continue;
			}
		}
		if ((couX==4)||(couX==3 && t))
		{
			x=1;
			break;
		}
		if ((couO==4)||(couO==3 && t))
		{
			o=1;
			break;
		}
	}

	if (x)
		return 1;
	if (o)
		return 2;

	int couX=0;
	int couO=0;
	bool t=0;
		
	for (int i=0; i<4; i++)
	{
		if (v[i][i]=='X')
			couX++;
		if (v[i][i]=='O')
			couO++;
		if (v[i][i]=='T')
			t=1;
	}
	if ((couX==4)||(couX==3 && t))
		x=1;
	if ((couO==4)||(couO==3 && t))
		o=1;

	if (x)
		return 1;
	if (o)
		return 2;

	couX=0;
	couO=0;
	t=0;
		
	for (int i=0; i<4; i++)
	{
		if (v[i][3-i]=='X')
			couX++;
		if (v[i][3-i]=='O')
			couO++;
		if (v[i][3-i]=='T')
			t=1;
	}
	if ((couX==4)||(couX==3 && t))
		x=1;
	if ((couO==4)||(couO==3 && t))
		o=1;
	
	if (x)
		return 1;
	if (o)
		return 2;
	if (!d)
		return 3;
	else
		return 4;
}

int main() 
{
	freopen("A-small-attempt1.in", "r", stdin); 
	freopen("output.txt", "w", stdout); 
	int n;
	cin>>n;
	vector <string> v(4);
	for (int i=0; i<4; i++)
	{
		v[i].resize(4);
	}

	string s;
	vector <int> res;
	for (int i=0; i<n; i++)
	{
		v.clear();
		v.resize(4);
		for (int i=0; i<4; i++)
		{
			v[i].resize(4);
		}
		for (int j=0; j<4; j++)
		{
			cin>>s;
			v[j]=s;
		}
		res.push_back(solve(v));
	}

	for (int i=0; i<res.size(); i++)
	{
		if (res[i]==1)
			cout<<"Case #"<<i+1<<": X won"<<endl;
		if (res[i]==2)
			cout<<"Case #"<<i+1<<": O won"<<endl;
		if (res[i]==3)
			cout<<"Case #"<<i+1<<": Draw"<<endl;
		if (res[i]==4)
			cout<<"Case #"<<i+1<<": Game has not completed"<<endl;
	}

//	_getch();
	return 0;
}