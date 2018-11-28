#include<bits/stdc++.h>
int main()
{
	int i,j,n,t,T,m,b,k,l;
	int a[5][5];
	char c[10001];
	char s[10001];
	a[1][1]=1;
	a[1][2]=2;
	a[1][3]=3;
	a[1][4]=4;
	a[2][1]=2;
	a[2][2]=-1;
	a[2][3]=4;
	a[2][4]=-3;
	a[3][1]=3;
	a[3][2]=-4;
	a[3][3]=-1;
	a[3][4]=2;
	a[4][1]=4;
	a[4][2]=3;
	a[4][3]=-2;
	a[4][4]=-1;
	int x,y;
	scanf("%d",&T);
	for(t=1;t<=T;++t)
	{
		scanf("%d%d",&l,&k);
		scanf("%s",c);
		for(i=0;i<k;++i)
			for(j=0;j<l;++j)
				s[i*l+j]=c[j];
		m=k*l;
		s[m]='\0';
		x=1;
		n=2;
		b=1;
		for(i=0;i<m;++i)
		{
			y=s[i]-103;
			x=a[x][y];
	//		if(i<15)
	//			printf("%dx %dy %di\n",x,y,i);
			if(x<0)
			{
				b=b*-1;
				x=-x;
			}	
			if(x==n)
			{
				x=1;
		//		printf("%di\n",i);
				n++;
			}
	//		if(n==5)
	//		{
	//			printf("%di %dx %db\n",i,x,b);
	//			break;
	//		}
		}
	//	printf("%dn %dx %db\n",n,x,b);
		if(n==5 && x==1 && b==1)
			printf("Case #%d: YES\n",t);
		else
			printf("Case #%d: NO\n",t);
	}
	return 0;
}
