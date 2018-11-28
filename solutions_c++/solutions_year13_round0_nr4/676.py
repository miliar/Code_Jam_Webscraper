#include<stdio.h>
#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
using namespace std;
#define fe(i,n) for(__typeof(n.begin()) i=n.begin();i!=n.end();i++)
map<int,int>g;
struct N
{
	int t;
	vector<int>l;
	void scan()
	{
		l.clear();
		scanf("%d",&t);
		int q,x;
		for(scanf("%d",&q);q--;)
		{
			scanf("%d",&x);
			l.push_back(x);
		}
	}
}b[50];
set<int>v;
int a[50];
int n;
void in(int i)
{
    --g[b[i].t];
    fe(k,b[i].l)
    	++g[*k];
}
void out(int i){
    ++g[b[i].t];
    fe(k,b[i].l)
    	--g[*k];
}
bool dfs(int k=0,int s=0)
{
	if(v.count(s))
		return 0;
    if(k==n)
	{
		for(int i=0;i<n;i++)
			cout<<a[i]+1<<" ";
		cout<<endl;
		return 1;
	}
	else
	{
		for(int i=0;i<n;i++)
			if(~s>>i&1)
				if(g[b[i].t])
				{
					a[k]=i;
					in(i);
					if(dfs(k+1,s|1<<i))
						return 1;
					out(i);
				}
		v.insert(s);
		return 0;
	}
}
int main()
{

	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int t,w=0,k;
	for(scanf("%d",&t);t--;)
	{
		cerr << t << endl;
		printf("Case #%d: ",++w);
        v.clear();
        g.clear();
        for(scanf("%d%d",&k,&n);k--;)
        {
			int x;
			scanf("%d",&x);
			g[x]++;
		}
        for(int i=0;i<n;i++)
        	b[i].scan();
        if(!dfs())
			puts("IMPOSSIBLE");
    }
}

