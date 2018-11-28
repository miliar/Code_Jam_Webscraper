# include<stdio.h>
# include<stdlib.h>
# include<string.h>
# include<math.h>
# define PI 3.14159265358979323846

FILE *input,*output;
int compare1(const void *a,const void *b )
{
	return *(long long*)a - *(long long*)b;
}
int compare2(const void* a,const void *b )
{
	return *(long long*)b - *(long long*)a;
}
int main()
{
	int T,x;
    long long N,i,sum,count,t,r,a,b;
   
    
	input  = fopen("A-small-attempt0.in","r");
	output = fopen("output.txt","w");
	fscanf(input,"%d",&T);
	
	
	
	for(x=1;x<=T;x++)
	{
		
		count =0;
		
		fprintf(output,"Case #%d: ",x);
		fscanf(input,"%lld%lld",&r,&t);
		
		
		
	
		a = r;
		b = r+1;
		while(t >= ((b*b)-(a*a)))
		{
			count++;
			t -=((b*b)-(a*a));
			a = a+2;
			b +=2;
		
		}
		
		
			
		fprintf(output,"%lld\n",count);
	
	}
return 0;	
}


