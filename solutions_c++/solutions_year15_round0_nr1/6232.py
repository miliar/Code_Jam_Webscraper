#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
double cas;
char max1[1001];
int main() {
	double digit[ 1000 ];
     int max;
	FILE *f = fopen("innew3.txt", "r");
	 FILE *f1 = fopen("outnew3.txt", "w");
    int c=0,i,up,ii;
    double num,len;
    fscanf(f, "%lf",&num);
    cas=num;
    for (ii=0; ii<cas; ii++) 
	{
    	c=0;
    	up=0;
        fscanf(f,"%lf",&max);
        fscanf(f,"%s",&max1);
    len=strlen(max1);    

    for(i=0;i<len;i++)
	{
		if (isdigit(max1[i])) {
        digit[i] = max1[i] - '0';
        if(up<i)
        {
        	c++;
        	up++;
        	up=digit[i]+up;
        }
        else
        up=up+digit[i];
        
	}
	
}
fprintf(f1,"Case #%d: %d \n", ii+1,c);
 }
    return 0;
}

