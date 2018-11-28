#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int judge(int s,int l, int r)
{
	if(l*r%s!=0)
		return 0;

	if(s==4)
	{

		if(l==4&&r==4)
			return 1;
		else if( l==4 &&r==3)
			return 1;
		else if(l==3&&r==4)
			return 1;
			return 0;
	}

	if(s==3)
	{
		if(l==3)
		{
			if(r>=2)
				return 1;
			return 0;
		}else
		{
			if(l>=2)
				return 1;
			return 0;
		}
	}
	return 1;
}
int main(int argc, char const *argv[])
{
			freopen("ds.in","r",stdin);
freopen("ds.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int c=1;c<=T;c++)
	{
		int s, l,r;
		int f=0;
		scanf("%d %d %d",&s,&l,&r);
		f=judge(s,l,r);
		if(f)
			printf("Case #%d: %s\n",c,"GABRIEL");
		else
			printf("Case #%d: %s\n",c,"RICHARD");
	}
	return 0;
}