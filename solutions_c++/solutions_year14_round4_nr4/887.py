#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<iostream>
#include<cstring>
using namespace std;

int trie[12][1010][30];
int size[12];
string str[10];
int n,m;
int val[10],sum[10];
int ans,num;

void insert(int id, string s)
{
	int len=s.size();
	int r=0;
	for(int i=0;i<len;i++)
    {
		int idx =s[i]-'A';
		if(trie[id][r][idx])
			r=trie[id][r][idx];
		else
        {
			trie[id][r][idx]=++size[id];
			r=trie[id][r][idx];
		}
	}
}

void dfs(int now)
{
	if(now>=n)
    {
		memset(sum,0,sizeof(sum));
		for(int i=0;i<n;i++)
			sum[val[i]]++;
		for(int i=0;i<m;i++)
			if(sum[i]==0)
                return;

		memset(trie,0,sizeof(trie));
		memset(size,0,sizeof(size));
		for(int i=0;i<n;i++)
			insert(val[i],str[i]);

		int temp=0;
		for(int i=0;i<m;i++)
			temp+=size[i];

		if(temp==ans)
			num++;
		else if(temp>ans)
        {
			ans=temp;
			num=1;
		}
	}
	else
	{
		for(int i=0;i<m;i++)
		{
			val[now]=i;
			dfs(now+1);
		}
	}
}

int main()
{
    int t,ys=0;
    freopen("D-small-attempt0.in","r",stdin);
    freopen("testD.out","w",stdout);

	scanf("%d",&t);

	while(t --)
    {
		scanf("%d%d",&n,&m);
        ans=0;
		num=0;

		for(int i=0;i<n;i++)
			cin>>str[i];

		dfs(0);
        ans+=m;
		printf("Case #%d: %d %d\n",++ys,ans,num);
	}
	return 0;
}
