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

bool check(int x,int r,int c)
{
    if(x==1) return 0;
    if(x==2)
    {
        if((r*c)%2==0) return 0;
        else return 1;
    }
    if(x==3)
    {
        if((r%3==0 && c%2==0) || (r%2==0 && c%3==0) || (r==3 && c==3)) return 0;
        else return 1;
    }
    if(x==4)
    {
        if((r==3 && c==4) || (r==4 && c==3) || (c==4 && r==4)) return 0;
        else return 1;
    }
}

int main()
{
 	#ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    int t,y;
    in(t);
    for (y=1;y<=t;y++)
    {
    	int x,r,c;
    	in(x);
    	inp(r,c);
    	if(check(x,r,c)) printf("Case #%d: RICHARD\n",y);
        else  printf("Case #%d: GABRIEL\n",y);
    }
	return 0;
}

