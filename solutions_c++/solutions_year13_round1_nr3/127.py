#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

int T;
int r,n,m,k;
int a[16];
int x[16];
int xx[16];
int b[65536][8];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for (int ww=1;ww<=T;ww++)
	{
		printf("Case #%d:\n",ww);
		scanf("%d%d%d%d",&r,&n,&m,&k);
		for (int www=1;www<=r;www++)
		{
			int es=0;
			for (int i=1;i<=k;i++) scanf("%d",a+i);
			for (int i=2;i<=m;i++)
				for (int j=2;j<=m;j++)
					for (int kk=2;kk<=m;kk++)
					{
						x[0]=i;
						x[1]=j;
						x[2]=kk;
						int mult=1;
						for (int d=0;d<1<<n;d++)
						{
							mult=1;
							for (int l=0;l<n;l++)
								if ((1<<l)&d) mult*=x[l];;
							xx[d]=mult;
						}
						bool can=true;
						for (int ii=1;ii<=k;ii++)
						{
							bool flag=false;
							for (int jj=0;jj<=1<<m;jj++)
								if (a[ii]==xx[jj]) flag=true;
							if (!flag) can=false;
						}
						if (can)
						{
							es++;
							b[es][0]=x[0];
							b[es][1]=x[1];
							b[es][2]=x[2];
						}
					}
			int ch=(rand()%es)+1;
			printf("%d%d%d\n",b[ch][0],b[ch][1],b[ch][2]);
		}
	}
    return 0;
}
