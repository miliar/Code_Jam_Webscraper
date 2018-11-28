#include<cstdio>
using namespace std;
int a1[4][4],a2[4][4];
int main()
{
	//freopen("A-small-attempt4.in","r",stdin);
	//freopen("out.out","w",stdout);
	int t,a,b,c;bool bl1,bl2;
	scanf("%d",&t);
	for(int ca=1;ca<=t;++ca)
	{
		printf("Case #%d: ",ca);
		bl1=0;bl2=0;
		scanf("%d",&a);--a;
		for(int i=0;i<4;++i)
		for(int j=0;j<4;++j)
			scanf("%d",a1[i]+j);
		scanf("%d",&b);--b;
		for(int i=0;i<4;++i)
		for(int j=0;j<4;++j)
			scanf("%d",a2[i]+j);
		for(int i=0;i<4;++i)
		for(int j=0;j<4;++j)
		if(a1[a][i]==a2[b][j])
		{
			if(bl1)
			{bl2=1;break;}
			bl1=1;c=a1[a][i];
		}
		if(bl2)puts("Bad magician!");
		else if(bl1)printf("%d\n",c);
		else puts("Volunteer cheated!");
	}
}
