#include<stdio.h>
#include<iostream>
using namespace std;
class A
{
	int count;
	int v;
	int a[10];
	void input(int vv);
	public:
	A(int vd);
	int input();
	//	void compute()
};
A::A(int vd)
{
	count=0;
	for(int i=0;i<10;i++)
		a[i]=0;
	v=vd;
}
void A::input(int vv)
{
	while(vv)
	{
		int t=vv%10;
		if(a[t]==1)
		{
		}
		else
		{
			a[t]=1;
			count++;
		}
		vv=vv/10;
	}
}
int A::input()
{
	for(int i=1;i<=99999;i++)
	{input(i*v);
//		printf("%d\n",i*v);
//		for(int y=0;y<=9;y++)
//			printf("%d ",a[y]);
//		printf("\n");
		if(count==10)
			return i*v;
	}
	return 0;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int j=1;j<=t;j++)
	{
		int v;
		scanf("%d",&v);
		A f(v);
		int u=f.input();
		if(u==0)
			printf("Case #%d: INSOMNIA\n",j);
		else
			printf("Case #%d: %d\n",j,u);
	}
}
