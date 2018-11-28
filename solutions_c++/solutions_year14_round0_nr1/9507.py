#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int exist(int x,int arr[5])
{
    for(int i=0; i<4; i++)
    {
        if(x==arr[i])
            return 1;
    }
    return 0;
}
int main()
{
    FILE* file;
    file=fopen("A-small-attempt1.in","r");
    int cases,first[5],second[5],claim,j,n,value,a,b,c,d;
    fscanf(file,"%d",&cases);
    for(int i=1; i<=cases; i++)
    {
        n=0;
        fscanf(file,"%d",&claim);
        for(j=0; j<claim; j++)
        {
            fscanf(file,"%d %d %d %d",&first[0],&first[1],&first[2],&first[3]);
        }

        for(j=claim; j<4; j++)
        {
            fscanf(file,"%d %d %d %d",&a,&b,&c,&d);
        }
        fscanf(file,"%d\n",&claim);
        for(j=0; j<claim; j++)
        {
            fscanf(file,"%d %d %d %d\n",&second[0],&second[1],&second[2],&second[3]);
        }

        for(j=claim; j<4; j++)
        {
            fscanf(file,"%d %d %d %d",&a,&b,&c,&d);
        }
        for(j=0; j<4; j++)
        {
            if(exist(first[j],second))
            {
                n++;
                value=first[j];
            }
        }
        switch(n)
        {
            case 0: printf("Case #%d: Volunteer cheated!\n",i);
                break;
            case 1: printf("Case #%d: %d\n",i,value);
                break;
            default: printf("Case #%d: Bad magician!\n",i);
                break;
        }
    }

    return 0;
}
