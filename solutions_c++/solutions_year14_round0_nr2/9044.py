#include <stdio.h>
#include <math.h>
#include <algorithm>

using namespace std;

int main()
{
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	
	int nt, t=1;
	scanf(" %d", &nt);
	
	while(nt--)
	{
		double c, f, x;
		scanf(" %lf %lf %lf", &c, &f, &x);
		
		int k = max(0, (int)ceil((x/c) - ((double)2.0/f) - (double)1));
		
		double time=0;
		
		for(int i=0; i<k; i++)
			time += c / (f*i + 2.0);
		
		time += x / (f*k + 2.0);
		
		printf("Case #%d: %.7lf\n", t++, time);
	}
	
	//fclose(stdin);
	//fclose(stdout);
	
	return 0;
}
