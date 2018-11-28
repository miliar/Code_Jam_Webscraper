#include<stdio.h>
double res[1000000];
int main()
{
    int zes;scanf("%d",&zes);
    for (int k=0;k<zes;k++)
    {
	double c,f,x;
	scanf("%lf%lf%lf",&c,&f,&x);
	res[0]= x/2.0;
	int wynik=0;
	for (int i=1;;i++)
	{
	    double dif = (f*x)/((2.0+f*(i-1.0))*(2.0+f*i)); 
	    res[i] = res[i-1] - dif +  c/(2.0+f*(i-1.0));
	    if(res[i]>res[i-1]) {wynik=i-1;break;}
	}
	printf("Case #%d: %.7lf\n",k+1,res[wynik]);
    }

}
