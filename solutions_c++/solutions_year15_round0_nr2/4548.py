#include <iostream>
#include <set>
#include <vector>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <climits>
#include <utility>
#include <map>
#include <sstream>
#include <cstring>
#define fore(i,m,n) \
for(int i=m;i<n;i++)
#define fori(i,m,n) \
for(int i=m;i<=n;i++)
#define T 1005
using namespace std;
vector<int> in;
int t;
bool compare(int i,int j)
{
	return i>j;
}
int minn(int i,int j,int k,int h)
{
	return min(min(i,j),min(h,k));
}
int minn2(int i,int j,int k)
{
	return min(min(i,j),k);
}
bool flag = false;
int dp(vector<int> a,int dec,int esp)
{
	int tmp,mn;
	t = a.size();
	if(dec==0 && flag)
	{
		fore(i,0,t)
			a[i]--;
	}
	else if(dec==1 && flag)
	{
		tmp = a[0];
		if(tmp%2==0)
		{
			a[0] = tmp/2; a.push_back(tmp/2);
		}
		else
		{
			a[0] = tmp/2+1; a.push_back(tmp/2);
		}
	}
	else if(dec==2 && flag)
	{
		if(a[0]<=2)
			return T;
		a[0]-=2;
		a.push_back(2);
	}
	else if(dec==3 && flag)
	{
		if(a[0]<=3)
			return T;
		a[0]-=3;
		a.push_back(3);
	}
	else if(dec==4 && flag)
	{
		if(a[0]<=4)
			return T;
		a[0]-=4;
		a.push_back(4);
	}
	
	sort(a.begin(),a.end(),compare);
	flag = true;
	
	if(a[0]<=3)
		return a[0] + esp;
	return min(minn(a[0]+esp,dp(a,0,esp)+1,dp(a,1,esp+1),dp(a,2,esp+1)),dp(a,3,esp+1));//,min(dp(a,3,esp+1),dp(a,4,esp+1)));
}


int main()
{
	int test,n,caso=0,mn,tmp,to,mx=0,esp;
	scanf("%d",&test);
	while(test--)
	{
		flag = false;
		int nueves=0;
		scanf("%d",&n);
		in.clear();
		in.resize(n);
		fore(i,0,n)
		{
			scanf("%d",&in[i]);
			if(in[i]==9)
				nueves++;
		}
		sort(in.begin(),in.end(),compare);
		mn = 9;
		if(nueves<4)
			mn = dp(in,0,0);
		printf("Case #%d: %d\n",++caso,mn);
	}
}	
