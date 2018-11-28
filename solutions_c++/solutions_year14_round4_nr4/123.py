#include<cstdio>
#include<algorithm>

struct str
{
	char s[100];
} a[100],p[100][100];
int pn[100];

inline bool operator <(const str &x,const str &y)
{
	int i;
	for(i=0;x.s[i]&&y.s[i];i++)if(x.s[i]!=y.s[i])break;
	return x.s[i]<y.s[i];
}

int max,maxcnt,n,m;

void backtracking(int x)
{
	int i,j,k,now;
	if(x==m)
	{
		for(i=0;i<n;i++)if(pn[i]==0)return;
		now=0;
		for(i=0;i<n;i++)for(j=0;j<pn[i];j++)
		{
			k=0;
			if(j)while(p[i][j].s[k]==p[i][j-1].s[k])k++;
			while(p[i][j].s[k])
			{
				k++;
				now++;
			}
		}
		if(now>max)
		{
			max=now;
			maxcnt=1;
		}
		else if(now==max)maxcnt++;
		return;
	}
	for(i=0;i<n;i++)
	{
		p[i][pn[i]]=a[x];
		pn[i]++;
		backtracking(x+1);
		pn[i]--;
	}
}

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int tc,tcn;
	scanf("%d",&tcn);
	for(tc=1;tc<=tcn;tc++)
	{
		int i,j;
		scanf("%d%d",&m,&n);
		for(i=0;i<m;i++)scanf("%s",a[i].s);
		std::sort(a,a+m);
		max=0;
		backtracking(0);
		printf("Case #%d: %d %d\n",tc,max+n,maxcnt);
	}
}