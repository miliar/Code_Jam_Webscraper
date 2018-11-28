#include<stdio.h>
#include<string>
#pragma warning(disable : 4996)
int num[27];
char s[2500];
int ans[11];
int main(void)
{
	freopen("C:\\Users\\user\\Desktop\\A-large.in","r",stdin);
freopen("C:\\Users\\user\\Desktop\\output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		memset(ans,0,sizeof(ans));
		memset(num,0,sizeof(num));
		memset(s,0,sizeof(s));
		scanf("%s",&s);
		int len=strlen(s);
		for(int j=0;j<len;j++)
		num[s[j]-'A']++;
		ans[0]=num['Z'-'A'];
		num['Z'-'A']=num['Z'-'A']-ans[0];
		num['E'-'A']=num['E'-'A']-ans[0];
		num['R'-'A']=num['R'-'A']-ans[0];
		num['O'-'A']=num['O'-'A']-ans[0];
		ans[2]=num['W'-'A'];
		num['T'-'A']=num['T'-'A']-ans[2];
		num['W'-'A']=num['W'-'A']-ans[2];
		num['O'-'A']=num['O'-'A']-ans[2];
		ans[6]=num['X'-'A'];
		num['S'-'A']=num['S'-'A']-ans[6];
		num['I'-'A']=num['I'-'A']-ans[6];
		num['X'-'A']=num['X'-'A']-ans[6];
		ans[8]=num['G'-'A'];
		num['E'-'A']=num['E'-'A']-ans[8];
		num['I'-'A']=num['I'-'A']-ans[8];
		num['G'-'A']=num['G'-'A']-ans[8];
		num['H'-'A']=num['H'-'A']-ans[8];
		num['T'-'A']=num['T'-'A']-ans[8];
		ans[3]=num['T'-'A'];
		num['T'-'A']=num['T'-'A']-ans[3];
		num['H'-'A']=num['H'-'A']-ans[3];
		num['R'-'A']=num['R'-'A']-ans[3];
		num['E'-'A']=num['E'-'A']-2*ans[3];
		ans[4]=num['R'-'A'];
		num['F'-'A']=num['F'-'A']-ans[4];
		num['O'-'A']=num['O'-'A']-ans[4];
		num['U'-'A']=num['U'-'A']-ans[4];
		num['R'-'A']=num['R'-'A']-ans[4];
		ans[5]=num['F'-'A'];
		num['F'-'A']=num['F'-'A']-ans[5];
		num['I'-'A']=num['I'-'A']-ans[5];
		num['V'-'A']=num['V'-'A']-ans[5];
		num['E'-'A']=num['E'-'A']-ans[5];
		ans[1]=num['O'-'A'];
		num['O'-'A']=num['O'-'A']-ans[1];
		num['N'-'A']=num['N'-'A']-ans[1];
		num['E'-'A']=num['E'-'A']-ans[1];
		ans[7]=num['S'-'A'];
		num['S'-'A']=num['S'-'A']-ans[7];
		num['E'-'A']=num['E'-'A']-2*ans[7];
		num['V'-'A']=num['V'-'A']-ans[7];
		num['N'-'A']=num['N'-'A']-ans[7];
		ans[9]=num['N'-'A']/2;
		printf("Case #%d: ",i);
		for(int k=0;k<=9;k++)
		{
			for(int n=1;n<=ans[k];n++)
			printf("%d",k);
		}
		printf("\n");	
	}
		
}
		

