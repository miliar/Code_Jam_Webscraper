#include<bits/stdc++.h>
using namespace std;
const int maxn=36;
vector<pair<int,int> > pp;
bool used[maxn];
char mp[maxn][maxn];
int num[5]={1,1,2,6,24};
int n,a[maxn];
bool check(int now)
{
	if(now==n)
	{
		for(int i=0;i<n;++i)
			if(!used[i])return false;
		return true;
	}
	else
	{
		bool flag=false;
		for(int i=0;i<n;++i)
			if(mp[a[now]][i]=='1'&&!used[i])
			{
				flag=used[i]=true;
				if(!check(now+1))return false;
				used[i]=false;
			}
		return flag;
	}
}
bool allcheck()
{
	for(int i=0;i<num[n];++i)
	{
		//cout <<i<<" "<<num[n]<<endl;
		//for(int i=0;i<n;++i)cout <<a[i]<<"-";cout <<endl;
		memset(used,0,sizeof(used));
		if(!check(0))return false;
		//cout <<i<<" "<<num[n]<<endl;
		next_permutation(a,a+n);
	}
	return true;
}
int cnt[1<<16];
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
int main()
{
	int T;
	scanf("%d",&T);
	cnt[0]=0;
	for(int i=1;i<(1<<16);++i)
		cnt[i]=cnt[i/2]+(i&1);
	for(int cas=1;cas<=T;++cas)
	{
		scanf("%d",&n);
		for(int i=0;i<n;++i)
		{
			a[i]=i;
			scanf("%s",mp[i]);
		}
		pp.clear();
		for(int i=0;i<n;++i)
			for(int j=0;j<n;++j)
				if(mp[i][j]=='0')pp.PB(MP(i,j));
		int k=pp.size();
		int res=k;
		for(int i=0;i<(1<<k);++i)
		{
			for(int j=0;j<k;++j)
				if(i>>j&1)mp[pp[j].FI][pp[j].SE]='1';
			if(allcheck())res=min(res,cnt[i]);
			for(int j=0;j<k;++j)
				if(i>>j&1)mp[pp[j].FI][pp[j].SE]='0';
		}
		printf("Case #%d: %d\n",cas,res);
	}
}
