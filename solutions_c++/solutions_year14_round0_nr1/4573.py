#include <cstdio>
#include <algorithm>

using namespace std;

int a[5][5];
int b[5][5];
int n,m,res1,res2;

int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	
	int Test;
	scanf("%d",&Test);
	for (int ii=1;ii<=Test;++ii)
	{
		printf("Case #%d: ",ii);
		scanf("%d",&res1);
		for (int i=1;i<=4;++i)
			for (int j=1;j<=4;++j)
				scanf("%d",&a[i][j]);
		scanf("%d",&res2);
		for (int i=1;i<=4;++i)
			for (int j=1;j<=4;++j)
				scanf("%d",&b[i][j]);
		
		int cnt=0;
		int res=-1;
		for (int i=1;i<=4;++i)
			for (int j=1;j<=4;++j)
				if (a[res1][i]==b[res2][j])
				{
					++cnt;
					res=a[res1][i];
				}
		if (cnt==1) printf("%d\n",res);
		if (cnt==0) printf("Volunteer cheated!\n");
		if (cnt>1) printf("Bad magician!\n");
	}
	
	return 0;
}

