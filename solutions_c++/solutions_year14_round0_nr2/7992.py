#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	freopen("c:\\11.in","r",stdin);
	freopen("c:\\out.txt","w",stdout);
	int t, tt=1;
	scanf("%d", &t);
	while (tt<=t)
	{
		double c,f,x;
		scanf("%lf %lf %lf", &c, &f, &x);
		double sum = 0;
		double speed = 2;
		double may1,may2;
		while(1) {
			may1 = x/speed;
			may2 = c/speed + x/(speed+f);
			//cout<<may1<<" "<<may2<<" "<<c/speed<<endl;

				if (may1<=may2){
					sum+=may1;
					break;
				}
				else{
					sum+=(c/speed);
					speed+=f;

				}
		}

		printf("Case #%d: %0.7lf\n", tt, sum);
		tt++;
	}
}