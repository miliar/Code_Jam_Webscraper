#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    freopen ("B-large.in","r",stdin);
	freopen ("output.in","w",stdout);
    double c,f,x,first,x1,x2,x3,tot;
	int t,j=1;
	scanf("%d",&t);
    while(j<=t)
	{
               first=2;tot=0;
		scanf("%Lf %Lf %Lf",&c,&f,&x);
		while(1)
		{
			x1=x/first;
			x2=first+f;
			x3=(c/first)+(x/x2);
			if(x3<x1)
			{
			tot=tot+(c/first);
        }
            else
			{
				tot=tot+(x/first);
				break;
			}
			first=first+f;
		}
		printf("Case #%d: ",j);
		printf("%.07f\n",tot);
	j++;
    }
//	system("pause");
	return 0;
}
