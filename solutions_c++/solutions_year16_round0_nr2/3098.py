#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <iterator>
#include <ctype.h>
#include <algorithm>
#include <iomanip>
#include <string>
#include <sstream>
#include <cstring>
using namespace std;
int main()
{
	char pa[100];
	FILE *fa= fopen("i2.txt", "r");
    FILE *fa1 = fopen("o2.txt", "w");
    int ca=0,la=0,ia,upa,iia,sa,ja,numa;
	fscanf(fa, "%d",&numa);
    for (iia=0; iia<numa; iia++)
	{
    	sa=0;
        fscanf(fa,"%s",&pa);
		la=strlen(pa);
		for(ia=la-1;ia>=0;ia--)
		{
			if (pa[ia]=='-')
			{
				sa++;
				for(ja=ia;ja>=0;ja--)
				{
					if(pa[ja]=='-')
						pa[ja]='+';
					else
						pa[ja]='-';
				}
			}
		}
		fprintf(fa1,"Case #%d: %d \n", iia+1,sa);
	}
	return 0;
}

