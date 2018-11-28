#include <stdio.h>     
#include <iostream>
#include <string.h>     
#include <cstdio>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <stack>
#include <fstream>
#include <sstream>
#pragma comment(linker, "/STACK:327772160")
using namespace std;
char Sum[10001];
bool F[10001];
bool zbs(int V)
{
	vector < int > P;
	while (V!=0)
	{
		P.push_back(V%10);
		V/=10;
	}
	for ( int i = 0 ; i < P.size() / 2; i ++)
	{
		if ( P[i]!=P[P.size() - 1 - i])
			return false;
	}
	return true;
}
bool check(int V)
{
	int t = (int)(sqrt(V+.0));
	if ( t*t==V)
	{
		if ( zbs(V) && zbs(t))
			return true;
		else return false;
	}
	else
		return false;
}

void Calc()
{
	for ( int i = 1; i <=10000; i ++)
	{
		F[i] = check(i);
	}
	for ( int i = 1; i <=10000; i ++)
	{
		int t = 0;
		if ( F[i])
		{
			t=1;
		}
		Sum[i] = Sum[i-1] + t;
	}
}
int main()
{
	//#ifndef _DEBUG
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
//#endif
	int T;
	scanf("%d",&T);
	Calc();
	for ( int k = 1 ; k <= T; k++)
	{
		int l , r;
		scanf("%d %d",&l,&r);
		printf("Case #%d: %d\n",k,Sum[r] - Sum[l-1]);
	}
	return 0;	
}