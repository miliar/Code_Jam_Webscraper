#include<stdio.h>
#include<stack>
using namespace std;

int main()
{
	int t,n,m,k,i,j,x;
	scanf("%d",&t);
	char ch;
	int a[5][5];
	a[1][1]=1;
	a[2][2]=a[3][3]=a[4][4]=-1;
	a[2][1]=a[1][2]=a[3][4]=2;
	a[4][3]=-2;
	a[3][1]=a[1][3]=a[4][2]=3;
	a[2][4]=-3;
	a[1][4]=a[4][1]=a[2][3]=4;
	a[3][2]=-4;
	for(i=0;i<t;i++)
	{
		scanf("%d %d",&m,&n);
int f=m;
		char b[m];
		int c[m*n];
	//	for(j=0;j<m;j++)
			scanf("%s",b);
//printf("%s",b);
		for(j=0;j<n;j++)
		{
			for(x=0;x<m;x++)
			{
				if(b[x]=='i')
					c[(j*m)+x]=2;
				if(b[x]=='j')
					c[(j*m)+x]=3;
				if(b[x]=='k')
					c[(j*m)+x]=4;
			}
		}


//for(j=0;j<m*n;j++)
//printf("%d\n",c[j]);

		int t1=c[0];
		x=0;
		for(j=1;j<m*n;j++)
		{
//printf("%d %d %d\n",j,x,t1);

			if(t1==2&&x==0)
			{
				x=2;
				t1=c[j];
				j++;
			}
			if(t1==3&&x==2)
			{
				x=3;
				t1=c[j];
				j++;
			}
			if(j<m*n)
			{
				if(t1<0&&c[j]<0)
					t1=a[-1*t1][-1*c[j]];
				else if(t1<0&&c[j]>0)
					t1=-1*a[-1*t1][c[j]];
				else if(t1>0&&c[j]<0)
					t1=-1*a[t1][-1*c[j]];
				else if(t1>0&&c[j]>0)
					t1=a[t1][c[j]]	;
			}	 		  
		}
		if(t1==4&&x==3)
			printf("case #%d: YES\n",i+1);
		else
			printf("case #%d: NO\n",i+1);
	}

	return 0;
}

















      


	























