#include <iostream>
#include <cstdio>
using namespace std;

int T;
int a[5][5],b[5][5];

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	int TT=0;
	while (TT<T)
	{
		++TT;
		int n,m;
		scanf("%d",&n);
		for (int i=1;i<=4;++i)
			for (int j=1;j<=4;++j)
				scanf("%d",&a[i][j]);
		scanf("%d",&m);
		for (int i=1;i<=4;++i)
			for (int j=1;j<=4;++j)
				scanf("%d",&b[i][j]);
		int num=0,k;
		for (int i=1;i<=4;++i)
			for (int j=1;j<=4;++j)
				if (a[n][i]==b[m][j])
				{
					++num;
					k=a[n][i];
				}
		printf("Case #%d: ",TT);
		if (num==0) printf("Volunteer cheated!\n");
		if (num==1) printf("%d\n",k);
		if (num>1) printf("Bad magician!\n");
	}
	return 0;
}