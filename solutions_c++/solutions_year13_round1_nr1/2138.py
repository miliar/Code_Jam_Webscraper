#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	freopen("G:\\A-small-attempt0.in","r",stdin);
	freopen("G:\\out.txt","w+",stdout);
	int T(0),r(0),t(0);
	int x(0),n(0);
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		scanf("%d %d",&r,&t);
		x=r+r+1;n=0;
		t-=x;
		while(t>=0)
		{
			n++;
			x+=4;
			t-=x;
		}
		printf("Case #%d: %d\n",i,n);
	}
	fclose(stdin);
	fclose(stdout);
}
