#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>

#define maxlongint 2147483647
#define LL long long
#define pb push_back
#define mp make_pair

using namespace std;

string st[10];
int bin[10],root[10],next[1000][30];
int T,m,n,cs=0;

int main()
{
	freopen("123.in","r",stdin);
	freopen("123.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d",&m,&n);
		for(int i=1;i<=m;i++)cin>>st[i];
		memset(bin,0,sizeof(bin));
		int maxnode=0,ans=0;
		while(!bin[0])
		{
			int node=0;
			memset(root,0,sizeof(root));
			memset(next,0,sizeof(next));
			for(int i=1;i<=m;i++)
			{
				if(!root[bin[i]])root[bin[i]]=++node;
				int now=root[bin[i]];
				for(int j=0,l0=st[i].size();j<l0;j++)
				{
					int p0=st[i][j]-64;
					if(!next[now][p0])next[now][p0]=++node;
					now=next[now][p0];
				}
			}
			if(node>maxnode)maxnode=node,ans=0;
			if(node==maxnode)ans++;
			int k=m;
			while(k && bin[k]==n-1)bin[k]=0,k--;
			bin[k]++;
		}
		printf("Case #%d: %d %d\n",++cs,maxnode,ans);
	}
	return 0;
}
