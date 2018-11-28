#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int cas;
int flag;
int main() {
     int ii, x,r,c,num;
	FILE *f = fopen("in2.txt", "r");
	 FILE *f1 = fopen("out3.txt", "w");
    fscanf(f, "%d",&num);
    cas=num;
    for (ii=0; ii<cas; ii++)
	{
		flag=1;
        fscanf(f,"%d %d %d",&x,&r,&c);

        if((x==1) && (x<=(r*c)))
            flag=0;
        if((x==2) && (((r*c)%x)==0) )
            flag=0;
        else if(x>2 && ( ((r*c)%x ==0) && ( (r>=x && c>=x-1) || (c>=x && r>=x-1))))
            flag=0;
        if(flag==0)
            fprintf(f1,"Case #%d: GABRIEL \n", ii+1);
        else
            fprintf(f1,"Case #%d: RICHARD \n", ii+1);

    }
    return 0;
}

