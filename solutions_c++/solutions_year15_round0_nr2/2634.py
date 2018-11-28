#include<iostream>
#include<cstdio>
#include<cstring>
#include<queue>
#include<cmath>
#include<algorithm>

using namespace std;
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
/*	int p[1005][2]={0};
	p[1][0]=0;p[1][1]=1;
	p[2][0]=0;p[2][1]=2;
	p[3][0]=0;p[3][1]=3;
	for(int i=4;i<=1000;i++)
	{
		int cou=0,a=(i+1)/2,b=i/2;
		cou++;
		p[i][0]=p[a][0]+p[b][0]+cou;
		p[i][1]=max(p[a][1],p[b][1]);
		if(1+max(a,b)<=p[i][0]+p[i][1])
		{
			p[i][0]=1;
			p[i][1]=max(a,b);
		}
	}
*/	int T,k=1;
	cin>>T;
	while(T--)
	{
		int n,t,a[1005]={0},temp,m=0;
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>temp;
			if(m<temp)
				m=temp;
			a[temp]++;
		}
		int ans=0x3f3f3f3f;
		for(int i=1;i<=m;i++)
		{
			int cou=0;
			for(int j=m;j>0;j--)
			{
				if(a[j]>0&&j>i)
				{
                    int t=a[j]*((j-1)/i);
                    cou+=t;
				}
			}
			if(ans>cou+i)
				ans=cou+i;
		}
		printf("Case #%d: %d\n",k++,ans);
	}
	return 0;
}

