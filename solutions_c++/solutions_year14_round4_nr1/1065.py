#include <iostream>
#include <stdio.h>
#include <utility>
#include <algorithm>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <math.h>
#include <cstdio>
#include <assert.h>
 
#define FOR(i,x,y) for(int i=(x);i<(y);i++)
#define RFOR(i,x,y) for(int i=(x);i>=(y);i--)
#define ABS(x) ((x)>0?(x):-(x))
#define SQ(x) ((x)*(x))
#define mset(x,y) memset(x,y,sizeof(x))
#define INF 1000000000
#define MOD 1000000007
#define pb(X) push_back(X) 
 
using namespace std;
 
typedef long long int lli;
typedef long double ld;
typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<double> vd;

int arr[10100];

int main()
{
	#ifndef ONLINE_JUDGE
    freopen("inp.txt","r",stdin);
    #endif

    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++)
    {
    	int n,x;
    	scanf("%d%d",&n,&x);

    	for(int i=0;i<n;i++) scanf("%d",&arr[i]);

    	int i=0,j=n-1;
    	sort(arr,arr+n);

    	int cnt=0;
    	while(i<=j)
    	{
    		if(i==j)
    		{
    			i++;
    			cnt++;
    		}
    		else if(arr[i]+arr[j]>x)
    		{
    			cnt++;
    			j--;
    		}
    		else
    		{
    			cnt++;
    			i++,j--;
    		}
    	}

    	printf("Case #%d: %d\n",tt,cnt);

    }


    return 0;
}