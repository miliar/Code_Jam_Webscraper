#include <cstdio>

using namespace std;

int cases;
double farmc, farmh, wins, tog, toc, cur, totes;

int main()
{
	scanf("%d", &cases);
	for(int q=1; q<=cases; q++)
	{
		tog=0;
		toc=0;
		cur=2;
		scanf("%lf%lf%lf", &farmc, &farmh, &wins);
		totes=wins/2;
		for(int k=0; true; k++)
		{
			toc=wins/cur;
			if(tog>totes)
				break;
			if(tog+toc<totes)
				totes=tog+toc;
			tog+=farmc/cur;
			cur+=farmh;
		}
		printf("Case #%d: %.7lf\n", q, totes);
	}
}

