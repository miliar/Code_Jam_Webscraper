#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<utility>
#include<vector>
#include<queue>
#include<stack>

#define ll long long int

using namespace std;

template<class T> void findMax(T &m, T x){m=m>x?m:x;}
template<class T> void findMin(T &m, T x){m=m<x?m:x;}
//const double pi=acos(-1);
int main()
	{
	int t, n, i, j, s, count, k;
	bool win;
	string a, b;
	char c;
	scanf("%d", &t);
	for(k=1;k<=t;k++)
	{
		scanf("%d", &n);
		cin>>a>>b;
		s=i=j=0;
		win=true;
		while(true)
		{
			if(i>=a.length() ^ j>=b.length())
			{
				win=false;
				break;
			}
			if(i>=a.length() && j>=b.length())
				break;
			c=a[i];
			count=0;
			while(i<a.length() && a[i]==c)
				{
					i++;
					count++;
				}
			if(b[j]!=c)
			{
				win=false;
				break;
			}
			while(j<b.length() && b[j]==c)
			{
				j++;
				count--;
			}
			s+=abs(count);
		}
		printf("Case #%d: ", k);
		if(!win)
			printf("Fegla Won\n");
		else
			printf("%d\n", s);
	}
	return 0;
	}
