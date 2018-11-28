#include <cstdio>
#include <cstdlib>
#include <cmath>

int main()
{
	double t , r;
	int cases ;

	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
      scanf("%d",&cases);

	for(int c = 1 ; c <= cases ; c++)
	{

		scanf("%lf%lf",&r,&t);

		double check=floor(((-2*r+1)+sqrt((2*r-1)*(2*r-1)+8*t))/4);

        if((2*check*check+(2*r-1)*check)  > t)
			check=check-1;

       printf("Case #%d: %.0lf\n",c,check);

	}

	return 0 ;
}
