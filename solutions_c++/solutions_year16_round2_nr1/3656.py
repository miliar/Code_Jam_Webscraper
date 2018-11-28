#include<cstdio>
#include<algorithm>
#include<iostream>
#include<cmath>
#include<cstring>
using namespace std;
#define inf 0x3f3f3f3f
#define eps 1e-9
#define ll long long
#define mod 100000000
int dfs(int pos);
int b[30][30],len1=0,a[50],c[50],d[5000],z=1;
char ch[5000];
int main()
{
	b[0][26]++;
	b[0]['E'-'A'+1]++;
	b[0]['R'-'A'+1]++;
	b[0]['O'-'A'+1]++;
	b[1]['E'-'A'+1]++;
	b[1]['O'-'A'+1]++;
	b[1]['N'-'A'+1]++;
	b[2]['T'-'A'+1]++;
	b[2]['W'-'A'+1]++;
	b[2]['O'-'A'+1]++;
	b[3]['T'-'A'+1]++;
	b[3]['R'-'A'+1]++;
	b[3]['H'-'A'+1]++;
	b[3]['E'-'A'+1]=2;
	b[4]['F'-'A'+1]++;
	b[4]['R'-'A'+1]++;
	b[4]['O'-'A'+1]++;
	b[4]['U'-'A'+1]++;
	b[5]['F'-'A'+1]++;
	b[5]['I'-'A'+1]++;
	b[5]['V'-'A'+1]++;
	b[5]['E'-'A'+1]++;
	b[6]['S'-'A'+1]++;
	b[6]['I'-'A'+1]++;
	b[6]['X'-'A'+1]++; 
	b[7]['S'-'A'+1]++;
	b[7]['E'-'A'+1]=2;
	b[7]['V'-'A'+1]++;
	b[7]['N'-'A'+1]++;
	b[8]['E'-'A'+1]++;
	b[8]['I'-'A'+1]++;
	b[8]['G'-'A'+1]++;
	b[8]['H'-'A'+1]++;
	b[8]['T'-'A'+1]++;
	b[9]['N'-'A'+1]++;
	b[9]['I'-'A'+1]++;
	b[9]['N'-'A'+1]++;
	b[9]['E'-'A'+1]++;
	freopen("in.in","r",stdin); //输入重定向，输入数据将从in.txt文件中读取 
	freopen("out.out","w",stdout); //输出重定向，输出数据将保存在out.txt文件中 
	int t;
	scanf("%d",&t);
	while(t--)
	{
		len1=0;
		memset(a,0,sizeof(a));
		memset(c,0,sizeof(c));
		memset(d,0,sizeof(d));
		scanf(" %s",ch);
		b[10][26];
		int len=strlen(ch);
		for(int i=0;i<len;i++)
		a[ch[i]-'A'+1]++;
		if(dfs(1))
		{
			printf("Case #%d: ",z++);
			for(int k=1;k<=len1;k++)
			printf("%d",d[k]);
			printf("\n");
		}
	 } 
	fclose(stdin);//关闭文件 
	fclose(stdout);//关闭文件 
	return 0;
}
int dfs(int pos)
{
	int i;
	for(i=1;i<=26;i++)
	{
		if(c[i]!=a[i])
		break;
	}
	if(i==27)
	return 1;
	int flag;
	for(int i=0;i<=9;i++)
	{
		flag=0;
		int j;
		for(j=1;j<=26&&!flag;j++)
		{
			c[j]+=b[i][j];
			if(c[j]>a[j])
			{
				flag=1;
				for(int k=1;k<=j;k++)
				c[k]-=b[i][k];
			}
		}
		if(!flag)
		{
			d[pos]=i;
			len1++;
			if(dfs(pos+1))
			return 1;
			else
			{
				for(int k=1;k<=j;k++)
				c[k]-=b[i][k];
				len1--;
			}	
		}
	}
	return 0;
}
