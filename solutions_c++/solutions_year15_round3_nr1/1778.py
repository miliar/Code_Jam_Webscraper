#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<vector>
#include<map>
using namespace std;

#define MOD 1000000007
#define llu long long unsigned
#define lld long long
#define ld long

int main ()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
	int x,t,n,i,j,r,c,w;
    cin>>t;
    for(i=0;i<t;i++)
    {
        cin>>r>>c>>w;
        x=(lld)ceil(((c*1.0)/w))+w-1;
        printf("Case #%d: %d\n",i+1,x);
    }

	return 0;
}
