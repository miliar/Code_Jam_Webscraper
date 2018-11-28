//(R-1)*(C/W如果有余数这里要再加1)+（C/W如果有余数再加1+W-1）
# include <iostream>
# include <cstdio>
using namespace std;
int R,C,W;
int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int i,q,t;
	scanf("%d",&q);
	for (i=1;i<=q;i++)
	{
		scanf("%d %d %d",&R,&C,&W);
		if (C%W)t=1;
		else t=0;
		printf("Case #%d: %d\n",i,(R-1)*(C/W+t)+(C/W+t+W-1));
	}
	return 0;
} 
