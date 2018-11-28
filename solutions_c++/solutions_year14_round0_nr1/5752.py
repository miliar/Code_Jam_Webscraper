#include<stdio.h>


int main()
{
    int c,t,r1,r2,i,j,k,flag, a[4][4], b[4][4],x=0,l[100],m[100];
    scanf("%d",&t);
    for(c=0; c<t; c++)
    {
        scanf("%d",&r1);
        for(j=0; j<4; j++)
            for(k=0; k<4; k++)
		scanf("%d",&a[j][k]);
	 scanf("%d",&r2);
	for(j=0; j<4; j++)
	    for(k=0; k<4; k++)
		scanf("%d",&b[j][k]);





        flag=0;
	for(i=0; i<4; i++)
            for(j=0; j<4; j++)
            {
		if(a[r1-1][i]==b[r2-1][j])
                {
		   flag++;
		   x=b[r2-1][j];
                }
	    }
	    l[c]=flag;
	    m[c]=x;


    }
    for(i=0; i<t; i++)
    {
	if(l[i]==0)
	printf("\nCase #%d: Volunteer cheated!",i+1);
	else if(l[i]==1)
	printf("\nCase #%d: %d",i+1,m[i]);
	else
	printf("\nCase #%d: Bad magician!",i+1);

       }


    return 0;
    }
