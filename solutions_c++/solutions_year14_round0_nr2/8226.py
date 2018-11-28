#include<bits/stdc++.h>

using namespace std;

int main ()
{
	double c , f , x , t1 , t2 , t3;
	int t , count , k;
	FILE *in , *out;
	
	in = fopen ("take.txt" , "r");
	out = fopen ("output.txt", "w");
	
	fscanf(in , "%d" , &t);
	
	for(k = 1; k <= t; k++)
	{
		fscanf(in , "%lf %lf %lf" , &c , &f , &x);
		
		t1 = 0.0;
		t2 = 0.0;
		t3 = 0.0;
		count = 0;
		
		while(t1 >= t2)
		{
				
			 t1 = t3 + x / (2 + count * f);
			 t2 = t3 + c / (2 + count * f) + x / (2 + (count + 1) * f);
			 t3 = t3 + c / (2 + count * f);
			 count ++;
		}
		
		fprintf(out , "Case #%d: %.7lf\n", k , t1);
		
	}
	
	return 0;
}
