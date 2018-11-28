#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<string>
#define LL long long
using namespace std;
int T,N;
struct Node
{
	char c;
	int num;
}f[50];
inline bool cmp(Node A,Node B)
{
	return A.num>B.num;
}
int cnt[500];
string ans;
inline void open()
{
	freopen("xx.in","r",stdin);
	freopen("xx.out","w",stdout);
}
int main()
{
	open();
	scanf("%d",&T);
	int cas=0;
	while(T--)
	{
		ans="";
		memset(cnt,0,sizeof(cnt));
		memset(f,0,sizeof(f));
		scanf("%d",&N);
		int sum=0;
		for(int i=1;i<=N;i++)
		{
			scanf("%d",&f[i].num);
			f[i].c=char(i+64);
			cnt[f[i].c]+=f[i].num;
			sum+=f[i].num;
		}
		while(1)
		{
			if(sum==0)
				break;
			sort(f+1,f+N+1,cmp);
			char ac=f[1].c;char ab=f[2].c;char ad=f[3].c;
			if(cnt[ac]==cnt[ab])
			{
				if(max(cnt[ac]-1,cnt[ad])<=(sum-2)/2)
				{ 
					ans+=ac;
					ans+=ab;
					sum-=2;
					if(sum!=0)
						ans+=" ";
					cnt[ac]--;cnt[ab]--;
					f[1].num--;f[2].num--;
				}
				else
				{
					ans+=ac;
					sum--;
					if(sum!=0)
						ans+=" ";
					cnt[ac]--;
					f[1].num--;
				//	sum--;					
				}
				continue;
			}			
			if(cnt[ac]==cnt[ab]+1)
			{
				
				ans+=ac;
				sum--;
				if(sum!=0)
					ans+=" ";
				cnt[ac]--;
				f[1].num--;
				continue;
			}		
			ans+=ac;
			ans+=ac;
			sum-=2;
			if(sum!=0)
				ans+=" ";
			cnt[ac]-=2;
			f[1].num-=2;
		}
		printf("Case #%d: ",++cas);
		cout<<ans<<endl;
	}
	return 0;
}
