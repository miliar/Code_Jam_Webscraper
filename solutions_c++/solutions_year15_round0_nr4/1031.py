#include <cstdio>
#include <iostream>

using namespace std;

int X,R,C;
int T;

bool Solve()/////////////////////////////
{
	int r = 0;
	int g = 0;

	if(X == 1)
	{
		g = 1;
		r = 0;
	}

	if(X == 2)
	{

		if(R%2 && C%2)
			r = 1;
		else
			g = 1;
	}

	if(X == 3)
	{
		if(R == 1 || C == 1)
			r = 1;

		else if(R%2 == 0 && C%2 == 0)
			r = 1;

		else
			g = 1;

	}

	if(X == 4)
	{
		int t1 = max(R,C);
		int t2 = min(R,C);

		if(t1 != 4 || t2 < 3)
			r = 1;
		else
			g = 1;
	}

	if(r == 1)
		return true;
	else
		return false;
}

int main()////////////////////////////////
{
	freopen("..\\D-small-attempt0.in","r",stdin);
	freopen("..\\D-small-attempt0.out","w",stdout);

//	freopen("..\\D-large.in","r",stdin);
//	freopen("..\\D-large.out","w",stdout);


	int d = 1;

	scanf("%d",&T);

	while(T--)
	{
		scanf("%d%d%d",&X,&R,&C);

		if(Solve())
			printf("Case #%d: RICHARD\n",d++);
		else
			printf("Case #%d: GABRIEL\n",d++);
	}
	return 0;
}
