#include <stdio.h>


int main(){
    int T; scanf("%d", &T);

    for (int Tcount = 1; Tcount <= T; Tcount++)
    {
    	double C,F,X;
    		scanf("%lf%lf%lf",&C,&F,&X);

    		double t=0;
    		double rate=2.0;

    		while(X/rate>C/rate+X/(rate+F))
    		{
    			t+=C/rate;
    			rate+=F;
    		}
    		t+=X/rate;
    printf("Case #%d: %lf\n", Tcount,t);


    }
    return 0;

}