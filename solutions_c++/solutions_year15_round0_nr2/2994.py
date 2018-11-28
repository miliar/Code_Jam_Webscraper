// ROH.cpp : Defines the entry point for the console application.
//


#include<iostream>
#include<vector>
#include<stdio.h>
#include<cstdio>
#include<map>
#include<stdlib.h>
#include<algorithm>
#include<queue>
#include<bitset>
#include<fstream>
#include<set>
#include<stack>
#include<utility>
#include<string>
#include<cstring>
#include<math.h>
#include<time.h>
using namespace std;

#define scan scanf_s
#define sscan sscanf_s
#define get gets_s
#define print printf 
#define mod 1000000007
#define ll long long
#define init int i,j,k,l,m,n,test
#define pause system("pause")
#define inf 1000000000

struct node
{
	int index;
	int freq;
};
bool operator<(const struct node &a, const struct node& b)
{
	if(a.freq!=b.freq)
	return (a.freq>b.freq);
	return (a.index>b.index);
}
vector<int> v[256];
	int a[1000009];
	char s[1000009];
int main()
{
	init;
	
	ifstream in("C:\\Users\\Ray\\Desktop\\google\\2\\B-large.in");
	ofstream out("C:\\Users\\Ray\\Desktop\\google\\2\\1_ans.txt");

	//scan("%lld",&test);
	
	in>>test;
	k=1;
	while(test--)
	{
		in>>n;
		int a[1009];
		m=0;
		for(i=0;i<n;i++)
		{
			in>>a[i];
			m=max(m,a[i]);
		}
		int real=inf;
		
		for(i=1;i<=m;i++)
		{
			int ans=0;
			for(j=0;j<n;j++)
			{
				if(a[j]>i)
				{
					ans+=(a[j]-i)/i;
					if((a[j]-i)%i!=0)
						ans++;
					
				}
			}
			ans+=i;
			real=min(real,ans);
		}
		
		out<<"Case #"<<k++<<": "<<real<<endl;
	}
	pause;
	
}