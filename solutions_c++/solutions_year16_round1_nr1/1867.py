#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <string.h>
long i,j,m,t;

long r,c,n,tmp;
 

void output(char str2[2002],int len)
{
    int i;
    for(i=0;i<len;i++)
        if(str2[i]!=-1)  printf( "%c",str2[i]);
    printf( "\n");
}
int main()  
{

    char str[1001];
    char str2[2002];
    char result[1001];
    int size,len;
    char max;
    int max_pos;
    int left;

    scanf("%ld",&t);

    for(m=1;m<=t;m++)
    {   
        printf( "Case #%ld: ",m);
        scanf("%s",str);
        size=strlen(str);
        for(i=0;i<size;i++)
            str2[i]=str[size-1-i];
        j=0;
        for(i=size-1;i<2*size;i++)
            str2[i]=str[j++];
        len=2*size-1;
        //此时str2下标从0到2*size-2，并且中点在size-1
        left=0;
        max=str2[left];max_pos=left;
        //for(i=0;i<=size-1;i++) printf("%d\n",str2[i]-str2[len-1-i] );
        while(max_pos<size-1)
        {

            max=str2[left];max_pos=left;
            for(i=left;i<=size-1;i++)
                if(str2[i]>=max) {max=str2[i];max_pos=i;}
             
            //printf("%d\n",max_pos );
            for(i=left;i<=max_pos;i++)
            {
                if(str2[i]==max)    {

                    if(i==size-1)  break;
                str2[len-1-i]=-1;}
                else      str2[i] =-1;
            }
            left=max_pos+1;
        }
        output( str2,len);
    }

    return 0;
}
