#include<stdio.h>
#include<string.h>
char c[2001];
int main()
{
int t,m=0;
	freopen("7.in","r",stdin);
		freopen("7f.out","w",stdout);
scanf("%d",&t);
while(t--)
{

	m+=1;
	int i,count[10];
	for(i=0;i<10;i++)
	{
		count[i]=0;
	}
	int a[26];
	for(i=0;i<26;i++)
		a[i]=0;
	scanf("%s",c);
	int length=strlen(c);
	for(i=0;i<length;i++)
	{
		a[c[i]-'A']+=1;
	}
	printf("Case #%d: ",m);
	while(a['Z'-'A']>0&&a['E'-'A']>0&&a['R'-'A']>0&&a['O'-'A']>0)
	{
		count[0]+=1;
		a['Z'-'A']-=1,a['E'-'A']-=1,a['R'-'A']-=1,a['O'-'A']-=1;
	}
		while(a['O'-'A']>0&&a['F'-'A']>0&&a['U'-'A']>0&&a['R'-'A']>0)
	{
		a['O'-'A']-=1,a['F'-'A']-=1,a['U'-'A']-=1,a['R'-'A']-=1;
		count[4]+=1;
	}
	while(a['T'-'A']>0&&a['W'-'A']>0&&a['O'-'A']>0)
	{
		a['T'-'A']-=1,a['W'-'A']-=1,a['O'-'A']-=1;
		count[2]+=1;
	}
		while(a['S'-'A']>0&&a['I'-'A']>0&&a['X'-'A']>0)
	{
		a['S'-'A']-=1,a['I'-'A']-=1,a['X'-'A']-=1;
		count[6]+=1;
	}
		while(a['T'-'A']>0&&a['H'-'A']>0&&a['R'-'A']>0&&a['E'-'A']>1&&a['E'-'A']>0)
	{
		count[3]+=1;
		a['T'-'A']-=1,a['H'-'A']-=1,a['R'-'A']-=1,a['E'-'A']-=2;
	}
	while(a['E'-'A']>0&&a['I'-'A']>0&&a['G'-'A']>0&&a['T'-'A']>0&&a['H'-'A']>0)
	{
		a['E'-'A']-=1,a['I'-'A']-=1,a['G'-'A']-=1,a['T'-'A']-=1,a['H'-'A']-=1;
		count[8]+=1;
	}
	
		while(a['S'-'A']>0&&a['N'-'A']>0&&a['E'-'A']>1&&a['E'-'A']>0&&a['V'-'A']>0)
	{
		a['S'-'A']-=1,a['N'-'A']-=1,a['E'-'A']-=2,a['V'-'A']-=1;
		count[7]+=1;
	}

		while(a['F'-'A']>0&&a['I'-'A']>0&&a['V'-'A']>0&&a['E'-'A']>0)
	{
		a['F'-'A']-=1,a['I'-'A']-=1,a['V'-'A']-=1,a['E'-'A']-=1;
		count[5]+=1;
	}
	

		while(a['N'-'A']>1&&a['E'-'A']>0&&a['I'-'A']>0)
	{
		a['N'-'A']-=2,a['E'-'A']-=1,a['I'-'A']-=1;
		count[9]+=1;
	}
	while(a['O'-'A']>0&&a['N'-'A']>0&&a['E'-'A']>0)
	{
		count[1]+=1;
		a['O'-'A']-=1,a['N'-'A']-=1,a['E'-'A']-=1;
	}
	//printf("\n");
	for(i=0;i<26;i++)
	{
		if(a[i]!=0)
		{
			printf("ERROR");
			break;
		}
	}
	for(i=0;i<10;i++)
	{
		while(count[i]--)
		{
			printf("%d",i);
		}
	}
	printf("\n");

}
}


