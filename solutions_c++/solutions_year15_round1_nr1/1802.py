//#include<bits/stdc++.h>
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<ctime>
#include<algorithm>
#include<queue>
#include<vector>
#include<set>
#include<stack>
#include<map>
#include<utility>

#define MAX 1000000007
#define mod 1000000007
#define ll long long
#define fo(i,in,end) for (i=in;i<end;i++)
#define rep(i,in,end) for (i=in;i<=end;i++)
#define in(x) scanf("%d",&x)
#define inp(x,y) scanf("%d%d",&x,&y)
#define vi vector <int>
#define vvi vector< vector <int> >
#define pii pair <int,int>
#define pb push_back
#define mem(a,val) memset(a,val,sizeof(a))
#define mp make_pair
#define tr(c,it) for (auto it=c.begin();it!=c.end();it++)
#define all(c) (c).begin(),(c).end()
#define F first
#define S second
using namespace std;

int main()
{
 	#ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    int t,x;
    in(t);
    for (x=1;x<=t;x++)
    {
    	int n,arr[1005],ans1,ans2,i,mx;
    	in(n);
    	rep(i,1,n)
    	{
    		in(arr[i]);
    	}
    	mx=-1,ans1=0;
    	rep(i,1,n-1)
    	{
    		if (arr[i+1]<arr[i])
    		{
    			ans1+=arr[i]-arr[i+1];
    			mx=max(mx,arr[i]-arr[i+1]);
    		}
    	}
    	if (mx<=0)
    	{
    		ans2=0;
    	}
    	else
    	{
    		ans2=0;
    		rep(i,1,n-1)
    		{
    			if (arr[i]<=mx)
    			{
    				ans2+=arr[i];
    			}
    			else
    			ans2+=mx;
    		}
    	}
    	printf("Case #%d: %d %d\n",x,ans1,ans2);
    }
	return 0;
}

