#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;
struct point{
	int x,y,z;
};

bool cmp(point a,point b)
{
	return a.z>b.z;
}
point a[50000];
int flag_heng[500],flag_shu[500],heng[500],shu[500];
int main()
{
	int ii,i,j,n,m,tt,t,x;
	bool d;
//	freopen("1.txt","r",stdin);freopen("2.txt","w",stdout);
//	freopen("B-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("B-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("B-large.in","r",stdin);freopen("A-large.out","w",stdout);
	scanf("%d",&tt);
	for(ii=1;ii<=tt;ii++)
	{
		scanf("%d%d",&n,&m);
		t=0;
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
			{
				scanf("%d",&x);
				t++;
				a[t].x=i;
				a[t].y=j;
				a[t].z=x;
			}
		sort(a+1,a+1+t,cmp);
		for(i=1;i<=n;i++)
		{
			flag_heng[i]=0;
			heng[i]=100;
		}
		for(j=1;j<=m;j++)
		{
			flag_shu[j]=0;
			shu[j]=100;
		}
		for(i=1;i<=t;i++)
		{
			d=false;
			if ((flag_heng[a[i].x]==1&&heng[a[i].x]==a[i].z)||(flag_heng[a[i].x]==0))
			{
				flag_heng[a[i].x]=1;
				heng[a[i].x]=a[i].z;
				d=true;
			}
			if ((flag_shu[a[i].y]==1&&shu[a[i].y]==a[i].z)||(flag_shu[a[i].y]==0))
			{
				flag_shu[a[i].y]=1;
				shu[a[i].y]=a[i].z;
				d=true;
			}
			if (d==false)  break;
		}
		if (d==false)  printf("Case #%d: NO\n",ii);
		else
			printf("Case #%d: YES\n",ii);

		
	}
	return 0;
}