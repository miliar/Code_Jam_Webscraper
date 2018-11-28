#include<iostream>
//#include<conio.h>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#define mod 1000000007

using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tc,t,i,j,k,n,m;
	int a[101][101];
    scanf("%d", &t);

	for(tc=1;tc<=t;++tc)
	{
		scanf("%d%d",&n,&m);

		for(i=0;i<n;++i)
		{
			for(j=0;j<m;++j)
			{
				scanf("%d",&a[n][m]);
			}
		}

		int f1,f2;
		for(i=0;i<n;++i)
		{
			for(j=0;j<m;++j)
			{
				f1=f2=0;
				if(a[n][m]==1)
				{
					for(k=0;k<n;++k)
					{
						if(a[k][j]!=1)
							f1=1;
					}
					for(k=0;k<m;++k)
					{
						if(a[i][k]!=1)
							f2=1;
					}
				}
				if(f1==1 && f2==1)
				{
					printf("Case #%d: NO\n",tc);
					goto q;
				}
			}
		}



	printf("Case #%d: YES\n",tc);
q:;
    }
	
//getch();
return 0;

}


