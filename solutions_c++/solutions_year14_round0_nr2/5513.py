#include<conio.h>
#include<cstdio>
using namespace std;

int main()
{
//	freopen("input.txt","r",stdin);

	int i,t;
	double C,F,X,time,t2,r;

	scanf("%d",&t);

	for(i=1;i<=t;i++)
	{
	    scanf("%Lf%Lf%Lf",&C,&F,&X);

	    r = 2.0;
	    time = X/r;
	    t2 = 0;
//        printf("%.7Lf\n",time);
	    for(;time>0;)
	    {
	        //buy farm
	        t2 = t2 + C/r;
            r = r+F;
            //check time
	        if(time > t2 + X/r)
            {
                time = t2 + X/r;
//                printf("%.7Lf\n",time);
//                getch();
            }
            else
                break;
	    }
	    printf("Case #%d: %.7Lf\n", i, time);
//	    printf("C = %.7Lf\nF = %.7Lf\nX = %.7Lf\n",C,F,X);
	}

	return(0);
}
