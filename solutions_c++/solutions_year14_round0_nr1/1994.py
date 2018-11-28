#include<cstdio>
using namespace std;


int main()
{freopen("A-small-attempt1.in","r",stdin);	
freopen ("Q1Ishan.txt","w",stdout);
	int T;
	scanf("%d",&T);
	int A[4][4];
	int B[4][4];
	int x,y;
	for(int k=1;k<=T;++k)
	{

	scanf("%d",&x);
	--x;
	for(int i=0;i<4;++i)
		{for(int j=0;j<4;++j)
			scanf("%d",&A[i][j]);
		}
	scanf("%d",&y);
	--y;
	for(int i=0;i<4;++i)
		{for(int j=0;j<4;++j)
			scanf("%d",&B[i][j]);
		}
	int t,f;
	f=0;
	for(int i=0;i<4;++i)
	{for(int j=0;j<4;++j)
		{if(A[x][i]==B[y][j])
			{t=A[x][i];
			++f;
			}
		}
	}
	printf("Case #%d: ",k);	
	if(f==0)
	{printf("Volunteer cheated!\n");
	}
	else if(f==1)
	{printf("%d\n",t);
	}	
	else
	{printf("Bad Magician!\n");
	}
}
}
