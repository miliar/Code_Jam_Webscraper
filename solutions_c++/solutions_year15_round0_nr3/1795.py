#include<stdio.h>
#include<string.h>
#include<algorithm>
#define N 1<<28
using namespace std;
int mul[8][8];
char a[N],ch[256];
int main()
{
	freopen("C-small-attempt0.in.txt","r",stdin);
	freopen("ans.txt","w",stdout);
	int i,j,len,t,tt=0,n,m,sum,ans;
	bool f;
	ch['1']=0;
	ch['i']=1;
	ch['j']=2;
	ch['k']=3;
	mul[0][0]=0;mul[0][1]=1;mul[0][2]=2;mul[0][3]=3;
	mul[1][0]=1;mul[1][1]=4;mul[1][2]=3;mul[1][3]=6;
	mul[2][0]=2;mul[2][1]=7;mul[2][2]=4;mul[2][3]=1;
	mul[3][0]=3;mul[3][1]=2;mul[3][2]=5;mul[3][3]=4;
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		{
			mul[i+4][j+4]=mul[i][j];
			mul[i+4][j]=mul[i][j+4]=(mul[i][j]+4)%8;
		}
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d%s",&n,&m,a);
		len=strlen(a);
		for(i=0;i<len;i++)
			a[i]=ch[a[i]];
		m=min(m,m%4+8);
		for(i=1;i<m;i++)
			memcpy(a+len*i,a,sizeof(char)*len);
		sum=0;
		len*=m;
		f=false;
		for(i=0;i<len;i++)
		{
			sum=mul[sum][a[i]];
			if(sum==1)
			{
				f=true;
				break;
			}
		}
		if(f)
		{
			f=false;
			for(sum=0,i++;i<len;i++)
			{
				sum=mul[sum][a[i]];
				if(sum==2)
				{
					f=true;
					break;
				}
			}
		}
		if(f)
		{
			for(sum=0,i++;i<len;i++)
				sum=mul[sum][a[i]];
			f=sum==3;
		}
		printf("Case #%d: %s\n",++tt,f?"YES":"NO");
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
/*
99
2 1
ik
3 1
ijk
3 1
kji
2 6
ji
1 10000
i

Case #1: NO
Case #2: YES
Case #3: NO
Case #4: YES
Case #5: NO
*/
