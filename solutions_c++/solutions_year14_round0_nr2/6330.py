#include <iostream>
#include <stdio.h>
#include <cmath>
using namespace std;

int main() {
    freopen("B-large.in","r",stdin);
    freopen("2_out_large.out","w",stdout);
	int t,p=0,k;
	double C,F,X,M,ans;
	scanf("%d",&t);
	while(t--)
	{

		ans=0;
		p++;
		scanf("%lf %lf %lf",&C,&F,&X);
		M=((X-C)*F)-(2*C);
		M=M/(C*F);
		if(M>0)
		k=ceil(M);
		else
		k=0;
		for(int i=0;i<k;i++)
		{
			ans=ans+(C/double(2+i*F));
		}
		ans=ans+(X/double(2+k*F));
		printf("Case #%d: ",p);
		printf("%0.7lf\n",ans);


	}
	fclose(stdin);
    fclose(stdout);
	return 0;
}
