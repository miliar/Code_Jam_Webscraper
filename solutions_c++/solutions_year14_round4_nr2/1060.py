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

int arr[1010];

// int cnt;
// void cntinv(int l, int h)
// {
// 	if(l>=h) return;
// 	int m=(l+h)/2;
// 	cntinv(l,m);
// 	cntinv(m+1,h);

// 	int i=l,j=m+1;
// 	int size=l;
// 	while(i<=m&&j<=h)
// 	{
// 		if(inv[i]<inv[j]) tinv[size++]=inv[i++];
// 		else
// 		{
// 			tinv[size++]=inv[j++];
// 			cnt+=(m-i+1);
// 		}
// 	}
// 	while(i<=m) tinv[size++]=inv[i++];
// 	while(j<=h)
// 	{
// 		tinv[size++]=inv[j++];
// 		cnt+=(m-i+1);
// 	}

// 	for(int i=l;i<=h;i++) inv[i]=tinv[i];
// }

int main()
{
	#ifndef ONLINE_JUDGE
    freopen("inp.txt","r",stdin);
    #endif

    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++)
    {
    	int n;
    	scanf("%d",&n);
    	for(int i=0;i<n;i++) scanf("%d",&arr[i]);

    	int cnt=0;
        int i=0,j=n-1;
        while(i<j)
        {
            int mp=i;
            for(int l=i;l<=j;l++) if(arr[mp]>arr[l]) mp=l;
            // cout<<mp<<" "<<j<<endl;
            if(j-mp<mp-i)
            {
                cnt+=j-mp;
                for(int l=mp;l<j;l++) swap(arr[l],arr[l+1]);
                j--;
            }
            else
            {
                cnt+=mp-i;
                for(int l=mp;l>i;l--) swap(arr[l-1],arr[l]);
                i++;
            }
            // for(int i=0;i<n;i++) cout<<arr[i]<<" ";
            // cout<<endl;
        }
    	printf("Case #%d: %d\n",tt,cnt);
    }


    return 0;
}