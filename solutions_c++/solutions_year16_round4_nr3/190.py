#include<cstdio>
#include<string>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
int a[10001];
int b[10001];
int c[101][101];
int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
//	freopen("C-large.in","r",stdin);
//	freopen("C-large.out","w",stdout);
	int T,k=0;
	scanf("%d",&T);
	while(T>0)
	{
		T--;
		k++;
		int r,c;
		scanf("%d%d",&r,&c);
		int i,j;
		int x1,x2;
		for(i=1;i<=2*(r+c);i+=2)
		{
			scanf("%d%d",&x1,&x2);
			a[x1]=x2;
			a[x2]=x1;
		}
		printf("Case #%d:\n",k);
		int n=r*c;
		memset(b,0,sizeof(b));
		bool flag1=false;
		while(b[0]==0)
		{
			int ii=1,jj=1;
			if(b[3]==1&&b[4]==1&&b[11]==1&&b[13]==1)
			{
				int xx=0;
			/*	for(i=1;i<=16;i++)
					printf("%d",b[i]);
				printf("\n");*/
			}
			bool flag=true;
			x1=0;
			while(jj<=c)
			{
				x1++;
				int i1=ii,j1=jj;
				int di=1,dj=0;
				while(i1!=r+1&&i1!=0&&j1!=0&&j1!=c+1)
				{
					if(b[(i1-1)*c+j1]==0)
					{
						int tt=di;
						di=dj;
						dj=tt;
					}
					else
					{
						int tt=di;
						di=-dj;
						dj=-tt;
					}
					i1+=di;
					j1+=dj;
				}
				if(j1==c+1)
					x2=i1+c;
				if(j1==0)
					x2=(r+1-i1)+c+c+r;
				if(i1==0)
					x2=j1;
				if(i1==r+1)
					x2=(c+1-j1)+c+r;
				if(a[x1]!=x2)
				{
					flag=false;
					//break;
				}
				jj++;
			}
			jj--;
			while(ii<=r)
			{
				x1++;
				int i1=ii,j1=jj;
				int di=0,dj=-1;
				while(i1!=r+1&&i1!=0&&j1!=0&&j1!=c+1)
				{
					if(b[(i1-1)*c+j1]==0)
					{
						int tt=di;
						di=dj;
						dj=tt;
					}
					else
					{
						int tt=di;
						di=-dj;
						dj=-tt;
					}
					i1+=di;
					j1+=dj;
				}
				if(j1==c+1)
					x2=i1+c;
				if(j1==0)
					x2=(r+1-i1)+c+c+r;
				if(i1==0)
					x2=j1;
				if(i1==r+1)
					x2=(c+1-j1)+c+r;
				if(a[x1]!=x2)
				{
					flag=false;
				//	break;
				}
				ii++;
			}
			ii--;
			while(jj>=1)
			{
				x1++;
				int i1=ii,j1=jj;
				int di=-1,dj=0;
				while(i1!=r+1&&i1!=0&&j1!=0&&j1!=c+1)
				{
					if(b[(i1-1)*c+j1]==0)
					{
						int tt=di;
						di=dj;
						dj=tt;
					}
					else
					{
						int tt=di;
						di=-dj;
						dj=-tt;
					}
					i1+=di;
					j1+=dj;
				}
				if(j1==c+1)
					x2=i1+c;
				if(j1==0)
					x2=(r+1-i1)+c+c+r;
				if(i1==0)
					x2=j1;
				if(i1==r+1)
					x2=(c+1-j1)+c+r;
				if(a[x1]!=x2)
				{
					flag=false;
				//	break;
				}
				jj--;
			}
			jj++;
			while(ii>=1)
			{
				x1++;
				int i1=ii,j1=jj;
				int di=0,dj=1;
				while(i1!=r+1&&i1!=0&&j1!=0&&j1!=c+1)
				{
					if(b[(i1-1)*c+j1]==0)
					{
						int tt=di;
						di=dj;
						dj=tt;
					}
					else
					{
						int tt=di;
						di=-dj;
						dj=-tt;
					}
					i1+=di;
					j1+=dj;
				}
				if(j1==c+1)
					x2=i1+c;
				if(j1==0)
					x2=(r+1-i1)+c+c+r;
				if(i1==0)
					x2=j1;
				if(i1==r+1)
					x2=(c+1-j1)+c+r;
				if(a[x1]!=x2)
				{
					flag=false;
				//	break;
				}
				ii--;
			}
			if(flag)
			{
				int xx=0;
				for(i=1;i<=r;i++)
				{
					for(j=1;j<=c;j++)
					{
						xx++;
						if(b[xx]==0)
							printf("\\");
						else
							printf("/");
					}
					printf("\n");
				}
				flag1=true;
				break;
			}
			j=n;
			while(b[j]==1)
			{
				b[j]=0;
				j--;
			}
			b[j]++;
		}
		if(!flag1)
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
