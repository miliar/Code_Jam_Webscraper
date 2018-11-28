#include <stdio.h>

int lastOne(int pp,int qq,int nowGe)
{
	if (nowGe>40)
		return 0;
	if (pp==0)
		return nowGe;
	if (qq&1)
		pp<<=1;
	else
		qq>>=1;
	if (pp>=qq)
	{
		if (lastOne(pp-qq,qq,nowGe+1))
			return nowGe;
	}
	else
		return lastOne(pp,qq,nowGe+1);
}
int main()
{
	//freopen(".in","r",stdin);
	//freopen(".txt","w",stdout);
	freopen("A-small-attempt0.in","r",stdin);
	freopen("subc-a-out.txt","w",stdout);
	int tt,pp,qq,an;
	scanf("%d",&tt);
	for (int ti=1;ti<=tt;ti++)
	{
		scanf("%d%*c%d",&pp,&qq);
		printf("Case #%d: ",ti);
		if ((an=lastOne(pp,qq,1)))
			printf("%d\n",an);
		else
			printf("impossible\n");
	}
	return 0;
}
