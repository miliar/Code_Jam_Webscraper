#include <iostream>

#include <string.h>

#include <stdio.h>

using namespace std;


int main()

{
    
    FILE *fp;

    fp = fopen("input.txt", "r");

    char str[100],sub[100],temp;

    int i,c,k,l,in,j,t,flag=0,count1=0,count2=0,tot=0,n,len;

    fscanf(fp,"%d",&t);

    for(c=1;c<=t;c++)

    {

        tot=0;

        fscanf(fp,"%s%d",&str,&n);

        len=strlen(str);

        for(i=0;i<len;i++)

        {

            for(j=0;j<len-i;j++)

            {

                for(k=i,in=0;k<=i+j;k++,in++)

                sub[in]=str[k];

                sub[in]='\0';

                count1=0;

                count2=0;

                flag=0;

                for(l=0;l<strlen(sub);l++)

                {

                    temp=sub[l];

                    if(temp!='a'&&temp!='e'&&temp!='i'&&temp!='o'&&temp!='u')

                    {

                        if(flag==0)

                        {

                            count2=1;

                            flag=1;

                        }

                        else

                        count2++;

                    }

                    else

                    {

                        flag=0;

                        if(count2>count1)

                            count1=count2;

                    }

                    if(l==strlen(sub)-1)

                    {

                        if(count2>count1)

                        count1=count2;

                    }

                }

                if(count1>=n)

                    tot++;

            }

        }

        printf("Case #%d: %d\n",c,tot);

    }

    fclose(fp);

}
