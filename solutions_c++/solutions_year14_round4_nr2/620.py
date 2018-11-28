#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

const int MAXN = 2001;
const int MAXM = 2000011;
const int MAXK = 201;
const int INF = 1000000001;
const double eps = 1e-5;

int a[MAXN];
struct Node
{
	int pos;
	int val;
}b[MAXN];

bool cmp(const Node& b1,const Node& b2)
{
	return b1.val<b2.val;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,cas,i,j,n,ans,pos,res1,res2;
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			b[i].val=a[i];
			b[i].pos=i;
		}
		sort(b,b+n,cmp);
		ans=0;
		for(i=0;i<n;i++)
		{
			pos=b[i].pos;
			for(j=pos-1,res1=0;j>=0;j--)
				if(a[j]>b[i].val)
					res1++;
			for(j=pos+1,res2=0;j<n;j++)
				if(a[j]>b[i].val)
					res2++;
			ans+=min(res1,res2);
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}