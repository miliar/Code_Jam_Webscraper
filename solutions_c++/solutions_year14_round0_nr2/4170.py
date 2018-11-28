#include <cstdio>

int main()
{
    int T;
	double c,f,x;
    scanf("%i", &T);
    for(int t=1; t<=T; t++)
    {
		scanf("%lf %lf %lf",&c,&f,&x);
		int f_c = 0;
		double cost,saved;
		do
		{
			cost = c/(2+f*f_c);
			saved = (x/(2+f*f_c)) - (x/(2+f*(f_c+1)));
			f_c++;
		}while(cost < saved);

		f_c--;
		double total_time = 0;
		for(int i = 0; i < f_c; i++)
		{
			total_time += (c/(2+(f*i)));
		}
		total_time += x/(2+f*f_c);
		printf("Case #%i: %.7f\n", t, total_time);
	}
}
