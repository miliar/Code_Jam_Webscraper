#include<stdio.h>
struct point
{
	int x,y;
}w[101];
int tp;
int ccw(point a,point b,point c)
{
	tp=(b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x);
	if(tp==0)return 0;
	return tp>0?1:-1;
}
int dis(point a,point b)
{
	return (a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y);
}
int t[11],res[10],Max,N;
bool v[10];
bool Intersect(point a,point b,point c,point d)
{
	if(d.x==a.x&&d.y==a.y)
	{
		if(ccw(a,b,c)!=0)return false;
		if(dis(a,b)+dis(a,c)>dis(b,c))return true;
		return false;
	}
	if(b.x==c.x&&b.y==c.y)
	{
		if(ccw(b,a,d)!=0)return false;
		if(dis(b,a)+dis(b,d)>dis(a,d))return true;
		return false;
	}
	int e=ccw(a,b,c),f=ccw(a,b,d),g=ccw(c,d,a),h=ccw(c,d,b);
	if(e==0 && f==0 && g==0 && h==0)
	{
		e=dis(a,c)-dis(a,b),f=dis(a,d)-dis(a,b),g=dis(b,c)-dis(a,b),h=dis(b,d)-dis(a,b);
		if(e<0&&f>0)return true;
		if(e>0&&f<0)return true;
		if(g<0&&h>0)return true;
		if(g>0&&h<0)return true;
		return false;
	}
	if(e*f>0||g*h>0)return false;
	if(e*f<0&&g*h<0)return true;
	if(e*f==0 && g*h<0)return true;
	if(g*h==0 && e*f<0)return true;
	return false;
}
void DFS(int a)
{
	int i,j;
	if(a==N)
	{
		int Sum=0;
		t[N]=t[0];
		if(t[1]==6&&t[2]==3&&t[3]==1&&t[4]==5&&t[5]==4&&t[6]==2&&t[7]==8&&t[8]==7)
		{
			a=a;
		}
		for(i=0;i<N;i++)
		{
			Sum+=w[t[i]].x*w[t[i+1]].y;
			Sum-=w[t[i]].y*w[t[i+1]].x;
		}
		if(Sum<0)Sum=-Sum;
		if(Max>=Sum)return;
		for(i=0;i<N;i++){
			for(j=i+1;j<N;j++){
				if(Intersect(w[t[i]],w[t[i+1]],w[t[j]],w[t[j+1]]))break;
			}
			if(j!=N)break;
		}
		if(i==N)
		{
			Max=Sum;
			for(i=0;i<N;i++)res[i]=t[i];
		}
	}
	for(i=0;i<N;i++)
	{
		if(!v[i])
		{
			v[i]=true;
			t[a]=i;
			DFS(a+1);
			v[i]=false;
		}
	}
}
int main()
{
	int i,TC,T=0;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&TC);
	while(TC--)
	{
		printf("Case #%d: ",++T);
		scanf("%d",&N);
		for(i=0;i<N;i++)
		{
			scanf("%d%d",&w[i].x,&w[i].y);
		}
		t[0]=0;
		v[0]=true;
		Max=0;
		DFS(1);
		if(Max==0)
		{
			Max=Max;
		}
		v[0]=false;
		for(i=0;i<N;i++)printf("%d ",res[i]);
		printf("\n");
	}
}