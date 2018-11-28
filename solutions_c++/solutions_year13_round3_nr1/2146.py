#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int findcons(int,int,char a[],int,int);
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output2.txt","w",stdout);
    int i,test,m,n,j,k;
    int start,fin,gap,len,counter;
    char str[1000000];
    scanf("%d",&test);
    for(m=0;m<test;m++)
    {
        scanf("%s %d",str,&n);
        len=strlen(str);
        counter=0;
        for(gap=n;gap<=len;gap++)
        {
            for(start=0;(start+gap-1)<len;start++)
            {
                fin=start+gap-1;
                if((j=findcons(start,fin,str,m+1,n))==1)
                    {
                        /*printf("\ntest=%d  ",m+1);
                        for(k=start;k<=fin;k++)
                            printf("%c",str[k]);
                        printf("\n");*/
                        counter++;
                    }
            }
        }
        printf("Case #%d: %d\n",m+1,counter);
    }
    return 0;
}
int findcons(int start,int fin,char a[],int test,int n)
{
    int i,j,check;
    //printf("\nstart=%d finish=%d test=%d n=%d\n",start,fin,test,n);
    for(i=start;i<=fin;i++)
    {
        check=1;
        for(j=i;j<=(i+n-1)&&(i+n-1)<=fin;j++)
        {
            if(a[j]=='a'||a[j]=='e'||a[j]=='i'||a[j]=='o'||a[j]=='u')
            {
                check=0;
                break;
            }
        }
        //printf("\ncheck=%d\n",check);
        if(check==1&&j>=(i+n))
        return 1;
    }
    return 0;
}
