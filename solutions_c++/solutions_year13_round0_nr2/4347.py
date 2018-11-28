#include<stdio.h>
#include<cstringt.h>
int a[100][100],l[100],c[100],x,y,lc[100],cc[100];//0未知 1必须 -1不能
int t;
bool well;
int max0(int a,int b)
{
	if(a>b)return a;
	else return b;
}
int min0(int a,int b)
{
	if(a>b)return b;
	else return a;
}
int main()
{
	FILE *in=fopen("B.in","r");
	FILE *out=fopen("B.out","w");
	int i,j,k;
	fscanf(in,"%d",&t);
	for(i=1;i<=t;i++)
	{
		fscanf(in,"%d%d",&x,&y);
		for(j=0;j<x;j++)
			for(k=0;k<y;k++)
				fscanf(in,"%d",&a[j][k]);
		for(j=0;j<x;j++)l[j]=-1,lc[j]=0;
		for(j=0;j<y;j++)c[j]=-1,cc[j]=0;
		for(j=0;j<x;j++)
			for(k=0;k<y;k++)
				l[j]=max0(l[j],a[j][k]),c[k]=max0(c[k],a[j][k]);

		well=1;
		for(j=0;j<x&&well;j++)
			for(k=0;k<y&&well;k++)
			{
				if(l[j]>c[k])
				{
					if(l[j]==a[j][k])
					{
						if(!lc[j])
							lc[j]=1;
						else if(lc[j]==-1){well=0;continue;}
						if(!cc[k])
							cc[k]=-1;
						else if(cc[k]==1){well=0;continue;}
					}
					else if(c[k]==a[j][k])
					{
						if(!cc[k])
							cc[k]=1;
						else if(cc[k]==-1){well=0;continue;}
					}
					else {well=0;continue;}
				}
				else if(l[j]<c[k])
				{
					if(l[j]==a[j][k])
					{
						if(!lc[j])
							lc[j]=1;
						else if(lc[j]==-1){well=0;continue;}
						
					}
					else if(c[k]==a[j][k])
					{
						if(!cc[k])
							cc[k]=1;
						else if(cc[k]==-1){well=0;continue;}
						if(!lc[j])
							lc[j]=-1;
						else if(lc[j]==1){well=0;continue;}
					}
					else {well=0;continue;}
				}
				else
					if(c[k]!=a[j][k]){well=0;continue;}
			}
		if(well) fprintf(out,"Case #%d: YES\n",i);
		else fprintf(out,"Case #%d: NO\n",i);

	}
	return 0;
}