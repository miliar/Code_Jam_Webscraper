#include<iostream>
#include<cstdlib>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;

int d[1010],n,cda[1010];

int deal(int avg,int lef,int fen)
{
	int tlef=fen-lef;
	int t1=0,t2=0;
	for(int i=1;i<=n;i++)
	{
		if(d[i]==avg)
			if(t1<tlef)
				t1++;
		if(d[i]==avg+1)
			if(t2<lef)
				t2++;
	}
//	printf("---%d %d ",avg,lef);
//	printf("%d %d %d\n",t1,t2,fen-t1-t2-1);
//	if(lef)
	return max(0,fen-t1-t2-1);
}
int times;
bool cmp(int a,int b)
{return a>b;}
int ans=0x7fffffff;
void search(int a,int b)
{
	int maxx=0,stop=0;
	for(int i=1;i<=a;i++)
		if(d[i]>maxx)
			maxx=d[i],stop=i;
	if(maxx+b<ans)
	{
		times=a; 
		memcpy(cda,d,sizeof(d));
	}
	ans=min(maxx+b,ans);
	int t=d[stop];
	if(t==1||b>ans)return;
	for(int i=1;i<=t/2;i++)
	{
		d[a+1]=d[stop]-i;
		d[stop]=i;
		search(a+1,b+1);
		d[stop]=t;
	}
}

int main()
{
//	freopen("b.in","r",stdin);
//	freopen("bb.out","w",stdout);
	int T ,x,r,c;
	scanf("%d",&T);
	for(int tcase=1;tcase<=T;tcase++)
	{
		printf("Case #%d: ",tcase);
		scanf("%d%d%d",&x,&r,&c);
		if(r>c)swap(r,c);
		if(x==1)printf("GABRIEL\n");
		if(x==2)
		{
			if(r*c%2==1)printf("RICHARD\n");
			else printf("GABRIEL\n");
		}
		if(x==3)
		{
			if((r!=1&&c==3)||(r==3))
				printf("GABRIEL\n");
			else printf("RICHARD\n");
		}
		if(x==4)
		{
			if(r==4&&c==4)	printf("GABRIEL\n");
			else if(r==3&&c==4)printf("GABRIEL\n");
			else printf("RICHARD\n");
		}
		
		

}
	return 0;
}

