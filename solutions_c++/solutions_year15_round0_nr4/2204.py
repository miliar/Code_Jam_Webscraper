#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <map>
#include <cstdlib>
#include <string>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <map>
#include <vector>
#include <climits>
#include <bits/stdc++.h>
#define lli long long int
#define gc getchar_unlocked
#define get(t) scanf("%d",&t)
void scanint(int &x)
{
	register int c=gc();
	x=0;
	for(;c<48||c>57;c=gc());
	for(;(c>47&&c<58);c=gc()){x=(x<<1)+(x<<3)+c-48;}
}
using namespace std;
int main()
{
	ifstream fin;
	ofstream fout;
	int t,t1=1;
	get(t);
	int x,r,c;
	while(t--)
	{
		int flag=1;
		get(x);
		get(r);
		get(c);
		if(r>c)
		{
			int t=r;
			r=c;
			c=t;
		}
		if(x==1||x==2)
		{
			if((r*c)%x==0)
				flag=1;
			else
				flag=0;
		}
		else if(x==3)
		{
			if(r==2&&c==3)
				flag=1;
			else if(r==3)
				flag=1;
			else
				flag=0;
		}
		else if(x==4)
		{
			if(r==3&&c==4)
				flag==1;
			else if(r==4)
				flag=1;
			else
				flag=0;
		}
		if(flag)
			printf("Case #%d: %s\n",t1++,"GABRIEL");
		else
			printf("Case #%d: %s\n",t1++,"RICHARD");
	}
	return 0;
}
