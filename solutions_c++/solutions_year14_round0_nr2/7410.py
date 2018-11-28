#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	int t,i,l,j;
	double c,f,x,k=2.0,m,sum[11000],tot=0.0;
	for(i=0;i<11000;i++)
	sum[i]=0.0;
	scanf("%d",&t);
	for(l=1;l<=t;l++)
	{
		k=2.0;
		tot=0.0;
		cin>>c>>f>>x;
		sum[0]=x/k;
		sum[1]=c/(k);
		j=1;
		while((x/k)>(sum[j]+x/(k+f)))
		{
			
			sum[j+1]=c/(k+f);
			k+=f,j++;
		}
	if(j!=0){	for(i=1;i<j;i++)
		tot+=sum[i];
		tot+=x/(k);}
		else
		tot=x/k;
		printf("Case #%d: %.7f\n",l,tot);
	}
	return 0;
}