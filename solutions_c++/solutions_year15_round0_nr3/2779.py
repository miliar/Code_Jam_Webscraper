#include<iostream>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<cstdlib>
#include<fstream>
#include<ctime>
#include<string>
using namespace std;
#define ll long long
#define mxn 100010
#define mxe 200010
#define inf 0x3f3f3f3f
//#define mp make_pair
#define pii pair<int,int>

int a[4][4]={{0,1,2,3},{1,0,3,2},{2,3,0,1},{3,2,1,0}};
int b[4][4];
char s1[10010];
int mp[200];

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("output.out","w",stdout);
	memset(b,0,sizeof(b));
	b[1][1]=b[2][2]=b[3][3]=b[1][3]=b[2][1]=b[3][2]=1;
	mp['1']=0; mp['i']=1; mp['j']=2; mp['k']=3;
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int l,x;
		scanf("%d%d",&l,&x);
		scanf("%s",s1);
		if(l==1)
		{
			printf("Case #%d: NO\n",t);
			continue;
		}
		char s2[10010]="";
		for(int i=0;i<x;i++)
			strcat(s2,s1);
		int len=l*x,sum=0,bsum=0;
		bool ok=0;
		for(int i=0;i<len;i++)
		{
			int v=mp[s2[i]];
			bsum=bsum^b[sum][v];
			sum=a[sum][v];
		}
		if(sum!=0||bsum!=1)
		{
			printf("Case #%d: NO\n",t);
			continue;
		}
		for(int i=0;i<=len-3;i++)
		{
			if(t==65) cout<<i<<endl;
			for(int j=i+1;j<=len-2;j++)
			{
			//	printf("i=%d,j=%d\n",i,j);
				int fi=0,fj=0,fk=0;
				int bi=0,bj=0,bk=0;
				for(int k=0;k<=i;k++)
				{
					int v=mp[s2[k]];
					bi=bi^b[fi][v];
					fi=a[fi][v];
			//		printf("v=%d,fi=%d,bi=%d\n",v,fi,bi);
				}
				if(fi!=1||bi)
					continue;
				for(int k=i+1;k<=j;k++)
				{
					int v=mp[s2[k]];
					bj=bj^b[fj][v];
					fj=a[fj][v];
			//		printf("v=%d,fj=%d,bj=%d\n",v,fj,bj);
				}
				if(fj==2&&bj==0)
				{
					ok=1;
					break;
				}
			}
			if(ok)
				break;
		}
		if(ok)
			printf("Case #%d: YES\n",t);
		else
			printf("Case #%d: NO\n",t);
	}
	return 0;
}





	










		


				





						




