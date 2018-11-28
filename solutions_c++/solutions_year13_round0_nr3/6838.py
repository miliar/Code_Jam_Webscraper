#include <stdio.h>
#include <conio.h>
#include <math.h>

int palin(double);

main(){
	int count,t,n,i;
	int llim,ulim,j;
	scanf("%d",&t);
	
	for(i=0;i<t;i++){
		count=0;		
		scanf("%d %d",&llim,&ulim);
		
		for(j=llim;j<=ulim;j++){
			if(palin(j)==1)
				if(sqrt(j)==(int)sqrt(j))
					if(palin(sqrt(j))==1)
						count++;
		}
		
		printf("\nCase #%d: %d\n",i+1,count);
	}
	
	getch();
}

int palin(double num){
	int a[20],i=0,count=0,length;
	int temp=num;
	double rnum=0;
	
	while(temp > 0){
		a[i++]=temp%10;
		temp/=10;
		count++;	
	}	
	
	length=count;
	
	for(i=0;i<count;i++,count--){
		if((a[i]!=a[count-1]))
			return 0;
		else	
			count--;
	}
	
	if(num != (int)num){
		for(i=0;i<length;i++)
			rnum+=(a[i]*pow(10,i));
	
		//printf("%f is rnum and num is %f\n",rnum,num);
	
		if(rnum == num){
		//	printf("%f  ",num);
			return 1;
		}
		return 0;
	}
	
	return 1;
}
