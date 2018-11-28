#include <stdio.h>

int main()
{
    int T;
    scanf("%d",&T);
    int t=1;

    while(t<=T){
	double C,F,X;
	scanf("%lf %lf %lf",&C,&F,&X);

	double now=X/2,tmp,use=0;
	int i=0;
	while(1){
	    use+=(C/(2+F*i));
	    tmp=use+X/(2+F*(i+1));
	    if(tmp<now) now=tmp;
	    else break;
	    i++;
	}
	printf("Case #%i: %.7lf\n",t++,now);
    }
    return 0;
}
