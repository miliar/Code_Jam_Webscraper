#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <fcntl.h>
#include <errno.h>
#include <unistd.h>
#include <string.h>


    int main()
    {
    double  c, f, x, time_taken=0.0,optimal_time, temp, total_time, step = 2.000000; 
    int  cases, count = 1;
    FILE *fp1,*fp2;
    
    fp1 = fopen("B-large.in","r");
    fp2 = fopen("output.out.cpp","w");
    
    fscanf(fp1,"%d",&cases); 

    for (int i =0;i<cases;i++)
    {
        fscanf(fp1,"%lf",&c); 
        fscanf(fp1,"%lf",&f);
        fscanf(fp1,"%lf",&x);
        time_taken=0.0;
        optimal_time = 0.0;
        total_time=0;
        step=2.0;
    
        while (time_taken <= optimal_time)
        {
            time_taken = c/step;
            optimal_time = x/step;
            temp = x/(f + step);
            
            if (time_taken + temp > optimal_time)  
            {
                total_time+=optimal_time;
                fprintf(fp2,"Case #%d: %.7lf\n",count,total_time); 
                count++;
                break;
            }
            else 
            {
                total_time+=time_taken;
                step = f+ step;
            }
        }
    }   
    fclose(fp1);
    fclose(fp2);
    getchar();
    return 0;
    
    }
