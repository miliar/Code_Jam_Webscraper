#include<bits/stdc++.h>
using namespace std;

const char lib[2][10]={"RICHARD","GABRIEL"};

int main()
{freopen("E:/in.txt","r",stdin);freopen("out.txt","w",stdout);
	int T,t,x,r,c,s;
	for(scanf("%d",&T),t=1;t<=T;t++)
	{
		scanf("%d%d%d",&x,&r,&c);
		if(x>6)
			s=0;
		else if(r*c%x)
			s=0;
		else if(max(r,c)<x)
			s=0;
		else if(min(r,c)<x-1-(x>5))
			s=0;
		else
			s=1;
		printf("Case #%d: %s\n",t,lib[s]);
	}
	return 0;
}
