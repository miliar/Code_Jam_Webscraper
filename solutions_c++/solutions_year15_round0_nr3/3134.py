#include<stdio.h>
int main()
{
	FILE *ip,*op;
	long long t,l=0,x=0,i,j,sign=1,k;
	char ch='1',in,flag='i';
	ip=fopen("C:\\Users\\rimpa\\Desktop\\input.txt","r");
	op=fopen("C:\\Users\\rimpa\\Desktop\\output.txt","a");
	fscanf(ip,"%lld",&t);
	//printf("%lld\n",t);
	//printf("%lld%lld\n",l,)
	for(i=1;i<=t;i++)
	{
		fscanf(ip,"%lld%lld",&l,&x);
		//printf("%lld% lld\n",l,x);
		fgetc(ip);
		for(j=1;j<=x;j++)
		{
			if(j>=2)
			{
				fseek(ip,-l,SEEK_CUR);
				//printf("%lld\n",j);
				//getchar();
			}
			for(k=1;k<=l;k++)
			{
				in=fgetc(ip);
				//printf("in= %c\n",in);
				if(ch=='1' && in=='i')
				{
					
					ch='i';
					if(sign==1)
					{
						sign=1;
					}
					else
					{
						sign=-1;
					}
				}
				else if(ch=='1' && in=='j')
				{
					
					ch='j';
					if(sign==1)
					{
						sign=1;
					}
					else
					{
						sign=-1;
					}
				}
				else if(ch=='1' && in=='k')
				{
					
					ch='k';
					if(sign==1)
					{
						sign=1;
					}
					else
					{
						sign=-1;
					}
				}
				else if(ch=='i' && in=='i')
				{
					
					ch='1';
					if(sign==1)
					{
						sign=-1;
					}
					else
					{
						sign=1;
					}
				}
				else if(ch=='i' && in=='j')
				{
					
					ch='k';
					if(sign==1)
					{
						sign=1;
					}
					else
					{
						sign=-1;
					}
				}
				else if(ch=='i' && in=='k')
				{
					
					ch='j';
					if(sign==1)
					{
						sign=-1;
					}
					else
					{
						sign=1;
					}
				}
				else if(ch=='j' && in=='i')
				{
					
					ch='k';
					if(sign==1)
					{
						sign=-1;
					}
					else
					{
						sign=1;
					}
				}
				else if(ch=='j' && in=='j')
				{
					
					ch='1';
					if(sign==1)
					{
						sign=-1;
					}
					else
					{
						sign=1;
					}
				}
				else if(ch=='j' && in=='k')
				{
					
					ch='i';
					if(sign==1)
					{
						sign=1;
					}
					else
					{
						sign=-1;
					}
				}
				else if(ch=='k' && in=='i')
				{
					
					ch='j';
					if(sign==1)
					{
						sign=1;
					}
					else
					{
						sign=-1;
					}
				}
				else if(ch=='k' && in=='j')
				{
					
					ch='i';
					if(sign==1)
					{
						sign=-1;
					}
					else
					{
						sign=1;
					}
				}
				else
				{
					
					ch='1';
					if(sign==1)
					{
						sign=-1;
					}
					else
					{
						sign=1;
					}
				}
				//printf("flag= %c ch= %c\n",flag,ch);
				if(ch==flag && sign==1)
				{
					ch='1';
					flag=flag+1;
				}
				//printf("flag= %c ch= %c sign= %lld\n",flag,ch,sign);
			}
		}
		fgetc(ip);
		if(flag=='l' && ch=='1' && sign==1)
			fprintf(op,"Case #%lld: YES\n",i);
		else
			fprintf(op,"Case #%lld: NO\n",i);
		flag='i';
		ch='1';
		sign=1;
	}
	return 0;
}
