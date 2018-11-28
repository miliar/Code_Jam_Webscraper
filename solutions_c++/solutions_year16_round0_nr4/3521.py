#include<stdio.h>
int main()
{
    int zes;
    scanf("%d",&zes);
    for (int z=0;z<zes;z++)
    {
	int k,c,s;
	scanf("%d%d%d",&k,&c,&s);
	printf("Case #%d:",z+1);
	for (int i=0;i<k;i++)
	    printf(" %d",i+1);
	printf("\n");

    }
}
