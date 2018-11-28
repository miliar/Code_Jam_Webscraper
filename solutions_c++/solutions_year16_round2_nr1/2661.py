#include<stdio.h>
#include<string.h>
#include<cstdlib>
#include<cassert>
int a[11]={0},b[91]={0};
int main()
{
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin != NULL );
	FILE *fout = freopen("A-large.out", "w", stdout);
	int t,i,k,l,m;
	char s[2001];
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%s",s);
		for(k=0;k<strlen(s);k++)
		{
			b[s[k]]++;
				
		}
		a[0]=b[90];
		a[2]=b[87];
		a[4]=b[85];
		a[6]=b[88];
		a[8]=b[71];
		a[5]=b[70]-b[85];
		a[7]=b[83]-b[88];
		a[9]=b[73]-a[6]-a[8]-a[5];
		a[1]=b[79]-a[0]-a[2]-a[4];
		a[3]=b[72]-a[8];
		printf("Case #%d: ",i);
		for(l=0;l<10;l++)
		{
			for(m=0;m<a[l];m++)
			{
			printf("%d",l);
		    }
		    a[l]=0;
			
		}
		printf("\n");
		for(m=65;m<=90;m++)
		{
			b[m]=0;
		}
	}
}
