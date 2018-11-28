#include<stdio.h>
int main()
{
	freopen("cook.txt","r",stdin);
	freopen("bro.txt","w",stdout);
	long long int k,t,si,i,l,x,j,co,tep,u;
	long long int pro[10][10],coi,cok;
	pro[1][1]=1;
	pro[1][2]=2;
	pro[1][3]=3;
	pro[1][4]=4;
	pro[2][1]=2;
	pro[2][2]=-1;
	pro[2][3]=4;
	pro[2][4]=-3;
	pro[3][1]=3;
	pro[3][2]=-4;
	pro[3][3]=-1;
	pro[3][4]=2;
	pro[4][1]=4;
	pro[4][2]=3;
	pro[4][3]=-2;
	pro[4][4]=-1;
	/*div[1][1]=1;
	div[1][2]=2;
	div[1][3]=3;
	div[1][4]=4;
	div[2][1]=-2;
	div[2][2]=1;
	div[2][3]=-4;
	div[2][4]=3;
	div[3][1]=-3;
	div[3][2]=4;
	div[3][3]=1;
	div[3][4]=-2;
	div[4][1]=-4;
	div[4][2]=-3;
	div[4][3]=2;
	div[4][4]=1;*/
	char s[10004];
	long long int q;
	scanf("%lld",&t);
	for(i=1;i<=t;i++)
	{
		q=0;
		si=1;
		coi=0;
		cok=0;
		tep=1;
		scanf("%lld%lld",&l,&x);
		scanf("%s",s);
		for(j=0;j<l;j++)
		{
			if(tep<0)
			{
				si=-1;
				tep=-1*tep;
			}
			else
			si=1;
			if(s[j]=='i')
			co=2;
			else if(s[j]=='j')
			co=3;
			else if(s[j]=='k')
			co=4;
			tep=si*pro[tep][co];
		}
		if(tep==1)
		{
			tep=1;
		}
		else if(tep==-1)
		{
			if(x%2)
			tep=-1;
			else
			tep=1;
		}
		else
		{
			if(x%2==0&&x%4!=0)
			tep=-1;
			else
			tep=1;
		}
		if(tep==-1)
		{
		tep=1;
		si=1;
		for(j=0;j<x&&q==0;j++)
		{
			for(k=0;k<l&&q==0;k++)
			{
				if(tep<0)
	    		{
				si=-1;
				tep=-1*tep;
		    	}
				else
				si=1;
				if(s[k]=='i')
				co=2;
				else if(s[k]=='j')
				co=3;
				else if(s[k]=='k')
				co=4;
				tep=si*pro[tep][co];
				if(tep==2)
				++coi;
				else if(tep==4&&coi>0)
				++cok;
				if(coi>0&&cok>0)
				{
					q=-1;
					break;
				}
			}
		}
		if(coi>0&&cok>0)
		printf("Case #%lld: YES\n",i);
		else
		printf("Case #%lld: NO\n",i);
		}
		else
		{
			printf("Case #%lld: NO\n",i);
		}
	}
	return 0;
}
