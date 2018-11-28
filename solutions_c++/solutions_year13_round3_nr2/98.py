/*
#include <stdio.h>
#include <string.h>
#include <math.h>
FILE* in=fopen("b.in","r");
FILE* out=fopen("b.out","w");
int pass(int x,int y,int n)
{
	if(x<0)x=-x;
	if(y<0)y=-y;
	if(x==0&&y==0&&n==0)return 1;
	if(n*(n+1)/2<(x+y))return 0;
	if((n*(n+1)/2-x-y)%2)return 0;
	return 1;
}
int add(int x,int y)
{
	if(x<0)x=-x;
	if(y<0)y=-y;
	return x+y;
}
void find(int x,int y,int n)
{
	if(x==0&&y==0&&n==0)
		return;
	if(pass(x,y-n,n-1))
	{
		find(x,y-n,n-1);
		fprintf(out,"N");
		return;
	}
	if(pass(x-n,y,n-1))
	{
		find(x-n,y,n-1);
		fprintf(out,"E");
		return;
	}
	
	if(pass(x+n,y,n-1))
	{
		find(x+n,y,n-1);
		fprintf(out,"W");
		return;
	}
	if(pass(x,y+n,n-1))
	{
		find(x,y+n,n-1);
		fprintf(out,"S");
		return;
	}
}
int main()
{
	int t,i,j,x,y,begin;
	
	fscanf(in,"%d",&t);
	for(i=0;i<t;i++)
	{
		fscanf(in,"%d%d",&x,&y);
		begin=(int)(sqrt((float)(2*add(x,y))+0.25)+0.5);
		if(begin<0)begin>0;
		while(begin*(begin+1)/2>add(x,y))begin--;
		if(begin<0)begin>0;
		while(!pass(x,y,begin))begin++;
		//fprintf(out,"Case #%d: ",i+1);
		find(x,y,begin);
		fprintf(out,"\n");
	}
	return 0;
}
*/