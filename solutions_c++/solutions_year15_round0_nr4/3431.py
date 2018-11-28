#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("Output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i = 0; i < T; ++i)
	{
		bool success = 0;
		int X,R,C;
		scanf("%d %d %d",&X,&R,&C);
		if(X == 1)success = 1;
		else if(X == 2 && R*C % 2 == 0)success = 1;
		else if(X == 3 && R*C > 3 && R*C % 3 == 0)success = 1;
		else if(X == 4 && R*C > 9 && R*C % 4 == 0)success = 1;
		if(success)printf("Case #%d: GABRIEL\n",i+1);
		else printf("Case #%d: RICHARD\n",i+1);
	}
	return 0;
}