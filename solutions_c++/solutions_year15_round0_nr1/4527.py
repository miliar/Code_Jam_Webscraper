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
	fin.open("A-large.in");
	fout.open("opl");
	int t,t1=1;
	fin>>t;
	while(t--)
	{
		int n;string str;
		fin>>n;
		fin>>str;
		int ans=0,fans=0;
		for(int i=0;i<=n;i++)
		{
			if(str[i]-48>0)
			{
				if(i>ans)
				{
					fans+=i-ans;
					ans=i;
				}
				ans+=(str[i]-48);
			}
		}
		fout<<"Case #"<<t1<<": "<<fans<<"\n";
		t1++;
	}
	return 0;
}
