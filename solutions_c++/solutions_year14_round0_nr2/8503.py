//#include<iostream.h>
#include<conio.h>
#include<stdio.h>

int main()
{
	//clrscr();
	int number=0;
	double c,f,x,rate,flag;
	double mintime,t2,t3;
	int s;
	
	FILE *fp,*fp2;
    fp=fopen("input.in","r");
	fp2=fopen("output.txt","w");
    fscanf(fp,"%d",&s);
     printf("%d",s);  
	while(number<s)
	{
		rate=2;
		t2=0;
		flag=0;
		fscanf(fp,"%lf",&c);
		fscanf(fp,"%lf",&f);
		fscanf(fp,"%lf",&x);	
		
		mintime=x/rate;
		while(flag!=1)
		{
	
			t2=t2+c/rate;
			rate=rate+f;
			t3=t2+(x/rate);
	
			if(mintime>t3)
				mintime=t3;
			else
				flag=1;
		}
		
		fprintf(fp2,"Case #%d: %.7lf\n",number+1,mintime);
		number++;
	
	}
	
	getch();
	return 0;
}




