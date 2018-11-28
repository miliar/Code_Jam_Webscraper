#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int tt;
	double c,ff,f,x;
	double sum;
	scanf("%d",&tt);
	for(int t=1;t<=tt;t++){
		ff=0.0;f=2.0;sum=0.0;
		scanf("%lf %lf %lf",&c,&ff,&x);
		if( (c-x) >= 0){	
			printf("Case #%d: ",t);
			printf("%.7lf",(x/f));
		}
		else
		{
			printf("Case #%d: ",t);
			while(1)
			{
				if( ( (c/f + x/(f+ff)) - (x/f) ) >= 0){
					sum += (x/f);
					break;
				}
				else{
					sum += (c/f);
					f += ff;
				}
			}
			printf("%.7lf",sum);
		}
		printf("\n");
	}
	return 0;
}
		
