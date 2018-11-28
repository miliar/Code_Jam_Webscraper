#include <stdio.h>
int main(void) {
	int test,num=1;
	float C,F,X,minima,temp,pos,sno;
	scanf("%d",&test);
	while(test--)
	{
		scanf("%f %f %f",&C,&F,&X);
		minima=sno=X/2;
		temp=2;
		while(1)
		{
			temp=(pos=temp)+F;
			sno=sno+(C-X)/pos+X/temp;
			if(sno<minima)
			minima=sno;
			else
			break;
		};
		printf("Case #%d: %f\n",num,minima);
		num++;
	};
	return 0;
}
