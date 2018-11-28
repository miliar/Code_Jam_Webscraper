#include<stdio.h>
#include<string.h>
char ringarr[109];
int siz;

int beginn()
{
	int i;	
	for(i=0;i<=siz-1;i++)
		{
			if(ringarr[i]=='-')
				return(i);
		}	
	return(-1);
}

char xori(char ch)
{
	if(ch=='+')
		return('-');
	else
		return('+');
}

void flippi(int L,int R)
{
	int i=L,j=R;
	char tempchar;
	
	while(i<=j)
		{
			tempchar=ringarr[i];
			ringarr[i]=xori(ringarr[j]);
			ringarr[j]=xori(tempchar);			
			i++;
			j--;
		}
}

int endd()
{
	int i;
	for(i=siz-1;i>=0;i--)
		{
			if(ringarr[i]=='-')
				return(i);
		}	
	return(-1);
}

int trueorfalse()
{
	int i;	
	for(i=0;i<=siz-1;i++)
		{
			if(ringarr[i]=='-')
				return(0);
		}	
	return(1);
}

int main()
{
//freopen("B-large.in", "r" , stdin);
//freopen ("shivangoutput2.out","w",stdout);
	int i,T,ans,endvar,beginvar;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
		{
			ans=0;
			scanf("%s",ringarr);
			siz=strlen(ringarr);
			while(1)
				{
					if(trueorfalse()==1)
						break;
					endvar=endd();
					beginvar=beginn();	
					if(beginvar>0)
						{
							flippi(0,beginvar-1);
							ans++;	
						}
					if(trueorfalse()==1)
						break;
					flippi(0,endvar);
					ans++;
				}
			printf("Case #%d: %d\n",i,ans);	
		}
//	fclose(stdout);
	return(0);
}



