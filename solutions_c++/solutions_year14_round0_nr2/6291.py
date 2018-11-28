//sums in a triangle
#include<iostream>
#include<cstdio>
#include<algorithm>
#include <fstream>
using namespace std;
typedef long double lf;



int main()
{
	FILE *in_file  = fopen("B-large.in", "r"); // read only 
    FILE *out_file = fopen("cookie_ouput.txt", "w"); // write only 
    int t = 0,counter = 1;
    fscanf(in_file,"%d",&t);
    while(t--)
    {
    	double c=0.0,f=0.0,x=0.0, a=2.0, output=0.0;
        fscanf(in_file,"%lf%lf%lf",&c,&f,&x);
		printf("%f %f %f\n",c,f,x); 
		double temp_time = 1, initial_rate = a,incremented_rate=a+f;
		while(temp_time > 0.0)
		{
			temp_time = x/initial_rate - (c/initial_rate + x/(incremented_rate));
			if(temp_time > 0.0)
			{
				output = output+ c/(initial_rate);
				initial_rate = initial_rate + f;
				incremented_rate= incremented_rate + f;
			}
		}
		output = output + x/(initial_rate); 
		fprintf(out_file,"Case #%d: %.7lf\n",counter,output);
		counter++;
	}    	
 		return 0;   
}
