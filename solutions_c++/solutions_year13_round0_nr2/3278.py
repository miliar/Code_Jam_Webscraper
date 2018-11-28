#include <stdio.h>
#include <string.h>
#include <queue>
using namespace std;
struct lawn
{
	int s[100][100];
	int m,n;
	lawn()
	{
		int i,j;
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				scanf("%d",&s[i][j]);
	}
	lawn(int nn,int mm)
	{
		n=nn;
		m=mm;
		int i,j;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				s[i][j]=100;
	}
	bool operator ==(lawn &b)
	{
		int i,j;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				if(b.s[i][j]!=s[i][j])return 0;
		return 1;
	}
};
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cas;
	int k,i,j;
	scanf("%d",&cas);
	for(k=1;k<=cas;k++)
	{
		vector<lawn> qu;
		printf("Case #%d: ",k);
		lawn ta;
		qu.push_back(lawn(ta.n,ta.m));
		bool suc=0;
		int pv=0;
		while(pv<qu.size())
		{
			lawn a=qu[pv];
			pv++;
			int p1,p2,max=-1;
			for(i=0;i<a.n;i++)
			{
				for(j=0;j<a.m;j++)
				{
					//printf("%d ",a.s[i][j]);
					if(a.s[i][j]!=ta.s[i][j]&&ta.s[i][j]>max)
					{
						p1=i;
						p2=j;
						max=ta.s[i][j];
					}
				}
				//puts("");
			}
			//puts("");
			if(max==-1)
			{
				suc=1;
				break;
			}
			lawn b=a;
			bool y=1;
			for(i=0;i<a.n;i++)
			{
				if(a.s[i][p2]>max)a.s[i][p2]=max;
				if(a.s[i][p2]<ta.s[i][p2])
				{
					y=0;
					break;
				}
			}
			for(i=0;i<qu.size();i++)
				if(qu[i]==a)y=0;
			if(y)qu.push_back(a);
			y=1;
			for(i=0;i<a.m;i++)
			{
				if(b.s[p1][i]>max)b.s[p1][i]=max;
				if(b.s[p1][i]<ta.s[p1][i])
				{
					y=0;
					break;
				}
			}
			for(i=0;i<qu.size();i++)
				if(qu[i]==b)y=0;
			if(y)qu.push_back(b);
		}
		if(suc)puts("YES");
		else puts("NO");
	}
	return 0;
}