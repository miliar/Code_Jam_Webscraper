#include "cstdio"
#include "algorithm"
using namespace std;
int t,x,r,c;
int main()
{
	scanf ("%d", &t);
	for (int v=1; v<=t; v++)
	{
		scanf ("%d%d%d", &x, &r, &c);
		if (x==1) printf("Case #%d: GABRIEL\n", v);
		else if (x==2)
		{
			if ((r*c)%2==0) printf("Case #%d: GABRIEL\n", v);
			else printf("Case #%d: RICHARD\n", v);
		}
		else if (x==3)
		{
			if ((r*c)%3==0 && min(r,c)>=2) printf("Case #%d: GABRIEL\n", v);
			else printf("Case #%d: RICHARD\n", v);
		}
		else if (x==4)
		{
			if ((r*c)%4==0 && min(r,c)>=3) printf("Case #%d: GABRIEL\n", v);
			else printf("Case #%d: RICHARD\n", v);
		}
	}

	return 0;
}