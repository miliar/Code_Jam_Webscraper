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
    int t,i;
    in(t);
    for (i=1;i<=t;i++)
    {
    	int n,total=0,ans=0,j;
    	char str[1007];
    	scanf("%d %s",&n,str);
    	//cout<<n<<" "<<str;
    	for (j=0;j<=n;j++)
    	{
    		if (total<j)
    		{
    			ans+=j-total;
    			total=j;
    		}
    		total+=str[j]-'0';
    	}
    	printf("Case #%d: %d\n",i,ans);
    }
	return 0;
}

