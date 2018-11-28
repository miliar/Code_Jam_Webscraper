#include<bits/stdc++.h>
using namespace std;

double gao(double C,double F,double X)
{
    double tempcost,t1,t2=100000,rate=2.0;
	tempcost=0.0;
	t1=X/rate+tempcost;
	//cout<<X<<" "<<t1<<endl;
	while(t1<t2)
	{
	    t2=t1;
	    tempcost=C/rate+tempcost;
        rate=rate+F;
        t1=X/rate+tempcost;		
	}
	return t2;
}

int main()
{
    int T,casen;
	double C,F,X,ans;
	scanf("%d",&T);
	for(casen=0;casen<T;casen++)
	{
	    scanf("%lf%lf%lf",&C,&F,&X);
		ans=gao(C,F,X);
		printf("Case #%d: %.7lf\n",casen+1,ans);
	}
    return 0;
}