#include<bits/stdc++.h>
using namespace std;

char result;
bool dfs(int now,int r,int p,int s)
{
	if(now==0)
	{
		if(r)result='R';
		else if(p)result='P';
		else result='S';
		return true;
	}
	else
	{
		//x+y=r;
		//y+z=p;
		//x+z=s;
		int x=(r+p+s)/2-p;
		int y=(r+p+s)/2-s;
		int z=(r+p+s)/2-r;
		if(x<0||y<0||z<0)return false;
		return dfs(now-1,x,y,z);
	}
}
const int maxn=1<<15;
char ans[maxn];
void get_ans(int l,int r,char res)
{
	if(l+1==r)
	{
		if(res=='P')ans[l]='P',ans[r]='R';
		else if(res=='S')ans[l]='P',ans[r]='S';
		else ans[l]='R',ans[r]='S';
	}
	else
	{
		int mid=l+r>>1;
		bool flag=false;
		if(res=='P')
		{
			get_ans(l,mid,'P');
			get_ans(mid+1,r,'R');
		}
		else if(res=='S')
		{
			get_ans(l,mid,'P');
			get_ans(mid+1,r,'S');
		}
		else
		{
			get_ans(l,mid,'R');
			get_ans(mid+1,r,'S');
		}
		for(int i=l;i<=mid&&!flag;++i)
			if(ans[i]>ans[mid+1+i-l])flag=true;
			else if(ans[i]<ans[mid+1+i-l])break;
		for(int i=l;flag&&i<=mid;++i)
			swap(ans[i],ans[mid+1+i-l]);
	}
}
int main()
{
	int T,n,r,p,s;
	scanf("%d",&T);
	for(int cas=1;cas<=T;++cas)
	{
		scanf("%d%d%d%d",&n,&r,&p,&s);
		if(dfs(n,r,p,s))
		{
			//cout <<result<<endl;
			get_ans(0,(1<<n)-1,result);
			ans[1<<n]='\0';
			printf("Case #%d: %s\n",cas,ans);
		}
		else printf("Case #%d: IMPOSSIBLE\n",cas);
	}
	return 0;
}
