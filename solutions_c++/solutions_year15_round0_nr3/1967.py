#include<bits/stdc++.h>

using namespace std;

const int mul[5][5]={{0,0,0,0,0},
					 {0,1,2,3,4},
					 {0,2,-1,4,-3},
					 {0,3,-4,-1,2},
					 {0,4,3,-2,-1}};

int n,m,T;
char s[10010];
int tra[256];
int L[10010],R[10010];

int calc(int x,int y)
{
	assert(x&&y);
	int flag=1;
	if (x<0) flag*=-1,x*=-1;
	if (y<0) flag*=-1,y*=-1;
	return mul[x][y]*flag;
}

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	
	scanf("%d",&T);
	tra['i']=2;
	tra['j']=3;
	tra['k']=4;
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d%d%s",&n,&m,s);
		int l=strlen(s);
		for(int i=1;i<m;i++)
			for(int j=0;j<l;j++)
				s[l*i+j]=s[j];
		l=n*m;
		s[l]=0;
		L[0]=tra[s[0]];
		for(int i=1;i<l;i++)
			L[i]=calc(L[i-1],tra[s[i]]);
		R[l-1]=tra[s[l-1]];
		for(int i=l-2;i>=0;i--)
			R[i]=calc(tra[s[i]],R[i+1]);
		int flag=1;
		for(int i=0;i<l&&flag;i++) if (L[i]==2)
		{
			int cur=1;
			for(int j=i+1;j+1<l&&flag;j++)
			{
				cur=calc(cur,tra[s[j]]);
				if (cur==3&&R[j+1]==4)
					flag=0;
			}
		}
		printf("Case #%d: %s\n",tt,flag?"NO":"YES");
	}
	return 0;
}

