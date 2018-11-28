//Przemysław Jakub Kozłowski
#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
typedef long double LD;

int t;
LD C, F, X;
LD twyn, wyn;

int main()
{
	scanf("%d", &t);

	for(int ti = 1;ti <= t;ti++)
	{
		scanf("%Lf%Lf%Lf", &C, &F, &X);
		wyn = X/(LD)2.0;
		twyn = 0;
		for(int num = 1;;num++)
		{
			twyn += C/((LD)2.0+(LD)(num-1)*F);
			if(twyn+X/((LD)2.0+(LD)num*F) < wyn)
				wyn = twyn+X/((LD)2.0+(LD)num*F);
			else break;
		}
		printf("Case #%d: %.7Lf\n", ti, wyn);
	}

	return 0;
}
