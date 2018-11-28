#include<stdio.h>
#include<string.h>

int main()
{
	//FILE *fp=fopen("b.in","r");
	//FILE *fp2 = fopen("bb2.out","w");
		long int t,n,p[2000],i,min,max,tot,index,i2,gf,z;
		
		FILE *fp=fopen("a.in","r");
	FILE *fp2 = fopen("b.out","w");
	
	fscanf(fp,"%ld",&t);
	for(long int r=1;r<=t;r++)
{
	fprintf(fp2,"Case #%ld: ",r);
		tot=0;
		index=0;
	fscanf(fp,"%ld",&n);
	
	for(i=1;i<=n;i++)
	{
		fscanf(fp,"%ld",&p[i]);
	
	}
	
	
	if(n==2)
	{
		tot=p[1]+p[2];
		X:{};
		if(p[1]>p[2]&&tot>2)
		{
			fprintf(fp2,"A ");
			p[1]--;
			tot--;
		}
		else if(p[1]<p[2]&&tot>2)
		{
			fprintf(fp2,"B ");
			p[2]--;
			tot--;
		}
		else if((p[1]==p[2])&&tot>2)
		{
			fprintf(fp2,"AB ");
			tot=tot-2;	
		}
		else if(tot==2)
		{
			fprintf(fp2,"AB\n");
			tot=tot-2;
		}		
		if(tot>0)
		{
			goto X;
		}
	}
	
	if(n>=3)
		{
			tot=0;
			for(gf=1;gf<=n;gf++)
			{
				tot=tot+p[gf];
			}
			//X:{};
			while(tot>2)
			{
				max=-1;
				for(i2=1;i2<=n;i2++)
				{
					if(p[i2]>max)
					{	
					index=i2;
					max=p[i2];
					}
				}
				//fprintf(fp2,"max= %ld\n",max);
				
					fprintf(fp2,"%c ",index+64);
	
					p[index]--;
				tot--;
				
			}
			if(tot==2)
			{
				for(z=1;z<=n;z++)
				{
				if(p[z]==1)
				fprintf(fp2,"%c",z+64);	
				
				}
			
				fprintf(fp2,"\n");
				tot=tot-2;
			}
			
		}
	}
	//fprintf(fp2,"Case #%lld: %lld\n",c,ans);
	return 0;
}
