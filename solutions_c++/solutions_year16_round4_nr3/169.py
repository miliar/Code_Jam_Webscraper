#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int dx[4]={1,0,-1,0};
const int dy[4]={0,-1,0,1};
bool b[110][110][4];
char ch[110][110];
int A[410];
int l[210],r[210],S1[210],S2[210];
int N,R,C;
int main()
{
	int i,j,_T,T,top,d,x,y,X,Y,d1;
	bool flag,flag2;
	freopen("C-large.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&T);
	for (_T=1;_T<=T;_T++)
	{
		printf("Case #%d:\n",_T);
		scanf("%d%d",&R,&C);
		N=R+C;
		for (i=1;i<=N;i++)
		{
			scanf("%d%d",&l[i],&r[i]);
			if (l[i]>r[i]) swap(l[i],r[i]);
			A[l[i]]=i; A[r[i]]=i;
		}
		flag=true;
		for (i=1;i<=N;i++)
			for (j=1;j<=N;j++)
				if (i!=j)
					if ((l[i]<l[j])&&(l[j]<r[i])&&(r[i]<r[j])) flag=false;
		memset(ch,'/',sizeof(ch));
		if (flag)
		{
			memset(b,true,sizeof(b));
			top=0;
			for (i=1;i<=2*N;i++)
			{
				if ((top==0)||(A[i]!=S1[top]))
				{
					top++; S1[top]=A[i]; S2[top]=i;
				}
				else
				{
					if (S2[top]<=C)
					{
						X=0; Y=S2[top];
					}
					else if (S2[top]<=R+C)
					{
						X=S2[top]-C; Y=C+1;
					}
					else if (S2[top]<=R+C+C)
					{
						X=R+1; Y=R+C+C-S2[top]+1;
					}
					else
					{
						X=R+R+C+C-S2[top]+1; Y=0;
					}
					top--;
					if (i<=C)
					{
						d=0; x=1; y=i;
					}
					else if (i<=R+C)
					{
						d=1; x=i-C; y=C;
					}
					else if (i<=R+C+C)
					{
						d=2; x=R; y=R+C+C-i+1;
					}
					else
					{
						d=3; x=R+R+C+C-i+1; y=1;
					}
					while ((x>=1)&&(x<=R)&&(y>=1)&&(y<=C))
					{
						b[x][y][(d+2)%4]=false; flag2=false;
						for (j=1;j<=4;j++)
							if (b[x][y][(d+j)%4])
							{
								d1=(d+j)%4; b[x][y][d1]=false;
								if ((d^d1)==1) ch[x][y]='/';
								else ch[x][y]='\\';
								x=x+dx[d1]; y=y+dy[d1]; d=d1;
								flag2=true; break;
							}
						if (!flag2)
						{
							flag=false; break;
						}
					}
					if ((x!=X)||(y!=Y)) flag=false;
				}
				if (!flag) break;
			}
		}
		if (flag)
			for (i=1;i<=R;i++)
			{
				for (j=1;j<=C;j++) printf("%c",ch[i][j]);
				printf("\n");
			}
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
