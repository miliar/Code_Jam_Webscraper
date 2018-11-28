#include <cstdio>
using namespace std;

// Main
int main(void)
{
	int tc, cs, X, R, C, tmp;

	// Read Input
	scanf("%d",&tc);
	for(cs=1;cs<=tc;cs++)
	{
		scanf("%d%d%d",&X,&R,&C);
		if(R>C)
		{
			tmp=R;
			R=C;
			C=tmp;
		}
		printf("Case #%d: ",cs);
		if(X==1) puts("GABRIEL");
		else if(X==2)
		{
			if(R==1)
			{
				if(C%2) puts("RICHARD");
				else puts("GABRIEL");
			}
			else if(R==2) puts("GABRIEL");
			else if(R==3)
			{
				if(C==3) puts("RICHARD");
				else puts("GABRIEL");
			}
			else puts("GABRIEL");
		}
		else if(X==3)
		{
			if(R==1) puts("RICHARD");
			else if(R==2)
			{
				if(C==3) puts("GABRIEL");
				else puts("RICHARD");
			}
			else if(R==3) puts("GABRIEL");
			else puts("RICHARD");
		}
		else
		{
			if(R>=3&&C==4) puts("GABRIEL");
			else puts("RICHARD");
		}
	}
	return 0;
}