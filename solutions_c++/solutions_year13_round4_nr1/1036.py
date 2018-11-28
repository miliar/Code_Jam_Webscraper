#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define mod 1000002013
#define md ((tr[x].l+tr[x].r)/2)
struct pp
{
	int l,r,v;
}
a[2000];
struct pp2
{
	int x,y,z;
	bool operator<(pp2 xx)const
	{
		return x<xx.x;
	}
}
b[4000];
struct node
{
	int l,r,v,mi,ma;
}
tr[10000];
int T,n,m,cnt,d[4000];
void build(int x,int l,int r)
{
	tr[x].v=0;
	tr[x].mi=0;
	tr[x].ma=0;
	tr[x].l=l;
	tr[x].r=r;
	if(l!=r)
	{
		build(x*2,l,md);
		build(x*2+1,md+1,r);
	}
}
void add(int x,int l,int r,int v)
{
	if(tr[x].l==l&&tr[x].r==r)
	{
		tr[x].v+=v;
		tr[x].mi+=v;
		tr[x].ma+=v;
		return;
	}
	if(r<=md)add(x*2,l,r,v);
	else if(l>md)add(x*2+1,l,r,v);
	else {
		add(x*2,l,md,v);
		add(x*2+1,md+1,r,v);
	}
	tr[x].ma=max(tr[x*2].ma,tr[x*2+1].ma)+tr[x].v;
	tr[x].mi=min(tr[x*2].mi,tr[x*2+1].mi)+tr[x].v;
}
int check(int x,int l,int r)
{
	if(tr[x].l==l&&tr[x].r==r)return tr[x].mi;
	if(tr[x].v)
	{
		add(x*2,tr[x].l,md,tr[x].v);
		add(x*2+1,md+1,tr[x].r,tr[x].v);
		tr[x].v=0;
	}
	if(r<=md)return check(x*2,l,r);
	else if(l>md)return check(x*2+1,l,r);
	else return min(check(x*2,l,md),check(x*2+1,md+1,r));
}
int checkl(int x)
{
	if(tr[x].l==tr[x].r)return tr[x].l;
	if(tr[x].v)
	{
		add(x*2,tr[x].l,md,tr[x].v);
		add(x*2+1,md+1,tr[x].r,tr[x].v);
		tr[x].v=0;
	}
	if(tr[x*2].ma)return checkl(x*2);
	else return checkl(x*2+1);
}
int checkr(int x)
{
	if(tr[x].l==tr[x].r)return tr[x].l;
	if(tr[x].v)
	{
		add(x*2,tr[x].l,md,tr[x].v);
		add(x*2+1,md+1,tr[x].r,tr[x].v);
		tr[x].v=0;
	}
	if(tr[x*2+1].ma)return checkr(x*2+1);
	else return checkr(x*2);
}
int calc(int x,int y)
{
	long long xx=d[y]-d[x];
	long long ans=xx*(xx-1)/2;
	ans=xx*(long long)n-ans;
	ans%=mod;
	return ans;
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&T);
	for(int tc=1;tc<=T;tc++)
	{
		printf("Case #%d: ",tc);
		scanf("%d%d",&n,&m);
		cnt=0;
		for(int i=1;i<=m;i++)
		{
			scanf("%d%d%d",&a[i].l,&a[i].r,&a[i].v);
			b[++cnt].x=a[i].l;
			b[cnt].y=i;
			b[cnt].z=0;
			b[++cnt].x=a[i].r;
			b[cnt].y=i;
			b[cnt].z=1;
		}
		sort(b+1,b+cnt+1);
		int cnt2=0;
		for(int i=1;i<=cnt;i++)
		{
			if(b[i].x!=b[i-1].x)cnt2++;
			d[cnt2]=b[i].x;
			if(b[i].z==0)a[b[i].y].l=cnt2;
			else a[b[i].y].r=cnt2;
		}
		build(1,1,cnt2);
		long long oans=0;	
		for(int i=1;i<=m;i++)
		{
			long long tmp=calc(a[i].l,a[i].r)%mod;
			tmp*=(long long)a[i].v;
			tmp%=mod;
			oans+=tmp;
			oans%=mod;
			if(a[i].l!=a[i].r)add(1,a[i].l,a[i].r-1,a[i].v);
		}
		long long ans=0;
		for(int i=1;i<=cnt2;i++)
			for(int j=cnt2;j>i;j--)
			{
				int num=check(1,i,j-1);
				if(num)
				{
					long long tmp=calc(i,j)%mod;
					tmp*=(long long)num;
					tmp%=mod;
					ans+=tmp;
					ans%=mod;
					add(1,i,j-1,-num);
				}
			}
		oans-=ans;
		oans%=mod;
		if(oans<0)oans+=mod;
		printf("%d\n",(int)oans);
	}
}
