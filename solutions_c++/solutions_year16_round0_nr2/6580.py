#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<string>
using namespace std;
struct node
{
	int bur;
}a[101],b[101];
int n,m,num,step;
char ch;char str[200];
int main()
{
	freopen("t.in","r",stdin);
	freopen("t.out","w",stdout);
	scanf("%d",&n);
	for(int ii=1;ii<=n;ii++)
	{
		scanf("%s",str);
		//cin>>str;
		m=strlen(str);
		//cout<<m<<endl;
		//cout<<(unsigned char)str[0]<<endl;
		//printf("%d",(int)str[0]);


		//cout<<"fuck"<<endl;
		for(int i=1;i<=m;i++)
		{
			ch=str[i-1];
			//cout<<(int)ch<<endl;
			if (ch=='+')
				a[i].bur=0;
			else
				a[i].bur=1;
		}
		step=0;
		for(int i=1;i<=m-1;i++)
		{
			if (a[m-i+1].bur==0)
				continue;
			int j=1;
			while(a[j].bur==0)
				j++;
			if (j!=1)
			{
			step++;
			for(int k=1;k<=j;k++)
				b[k].bur=1-a[j-k+1].bur;
			for(int k=1;k<=j;k++)
				a[k].bur=b[k].bur;
			}
			step++;
			for(int k=1;k<=m-i+1;k++)
				b[k].bur=1-a[m-i+1-k+1].bur;
			for(int k=1;k<=m-i+1;k++)
				a[k].bur=b[k].bur;
		}
		if (a[1].bur==1)
			step++;
		printf("Case #%d: %d\n",ii,step);
	}
}
