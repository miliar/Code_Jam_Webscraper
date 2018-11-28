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
int ans=10000,*val,n,n1;
void scanint(int &x)
{
	register int c=gc();
	x=0;
	for(;c<48||c>57;c=gc());
	for(;(c>47&&c<58);c=gc()){x=(x<<1)+(x<<3)+c-48;}
}
using namespace std;
int calc()
{
	int x=val[n1-1]/2;
	if(val[n1-1]==9)
	{
		if(n1-2>=0)
		{
			if(val[n1-2]<4||val[n1-2]==6)
			{
				val[n1-1]=3;
				val[n1++]=6;
			}
			else
			{
				val[n1-1]=x;
				val[n1++]=x+1;
			}
		}
		else
		{
			val[n1-1]=3;
			val[n1++]=6;
		}
	}
	if(val[n1-1]%2==0)
	{
		val[n1-1]=x;
		val[n1++]=x;
	}
	else
	{
		val[n1-1]=x;
		val[n1++]=x+1;
	}
	sort(val,val+n1);
	/*for(int i=0;i<n1;i++)
		cout<<val[i]<<" ";
	cout<<endl;*/
	return val[n1-1];
}
int main()
{
	ifstream fin;
	ofstream fout;
	int t,t1=1;
	get(t);
	while(t--)
	{
		get(n);
		val=new int[5000+n];
		for(int i=0;i<n;i++)
			get(val[i]);
		/*cout<<n<<":: ";
		for(int i=0;i<n;i++)
			cout<<val[i]<<" ";
		cout<<endl;*/
		n1=n;
		sort(val,val+n1);
		int ref=4,t=0;
		if(val[n1-1]>3)
		{
			ans=val[n1-1];
			while(ref>3)
			{
				ref=calc();
				t++;
				//cout<<ref<<endl;
				ans=min(ans,t+ref);
			}
		}
		else
			ans=val[n1-1];
		printf("Case #%d: %d\n",t1++,ans);
	}
	return 0;
}
