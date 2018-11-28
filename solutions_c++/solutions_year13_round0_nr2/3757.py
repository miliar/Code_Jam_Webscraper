#include<stdio.h>
#include<conio.h>
int test(int a[100][100],int N,int M)
{
	int i,j,k,flag1,flag2;
	for(i=0;i<N;++i)
	{
		for(j=0;j<M;++j)
		{
			flag1=1;
			for(k=0;k<M;++k)
			{
				if(a[i][k]>a[i][j])
				{
					flag1=0;
					break;
				}
			}
			flag2=1;
			for(k=0;k<N;++k)
			{
				if(a[k][j]>a[i][j])
				{
					flag2=0;
					break;
				}
			}
			if(!flag1&&!flag2)
			{
				return 0;
			}
		}
	}
	return 1;
}
main()
{
	int T,M,N,a[100][100],set,i,j;
	clrscr();
	FILE *in=fopen("in.txt","r");
	FILE *out=fopen("out.txt","w");
	fscanf(in,"%d",&T);
	for(set=1;set<=T;++set)
	{
		fscanf(in,"%d %d",&N,&M);
		for(i=0;i<N;++i)
			for(j=0;j<M;++j)
				fscanf(in,"%d",&a[i][j]);
		if (test(a,N,M))
		{
			fprintf(out,"Case #%d: YES\n",set);
		}
		else
		{
			fprintf(out,"Case #%d: NO\n",set);
		}
	}
	fclose(in);
	fclose(out);
	getch();
	return 0;
}