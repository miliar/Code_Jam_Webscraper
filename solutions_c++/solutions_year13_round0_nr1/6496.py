#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>

using namespace std;

int check_angle(char arr[5][5])
{
    char result,temp,temp2;
    int t,i,l,k;

    temp=arr[0][0];

    if(temp!='.')
    {
        if(temp=='T')
            temp=arr[1][1];

        if(temp!='.')
        {
            temp2=temp;

            for(k=0;k<4;k++)
                if((arr[k][k]!=temp)&&(arr[k][k]!='T'))
                {
                    temp2='A';
                    break;
                }

            if(temp==temp2)
            {
                result=temp;
                printf("%c won\n",result);
                return 1;
            }
        }
    }

    return 0;
}

int check_angle2(char arr[5][5])
{
    char result,temp,temp2;
    int t,i,l,k;

    temp=arr[0][3];

    if(temp!='.')
    {
        if(temp=='T')
            temp=arr[1][2];

        if(temp!='.')
        {
            temp2=temp;

            for(k=0;k<4;k++)
                if((arr[k][3-k]!=temp)&&(arr[k][3-k]!='T'))
                {
                    temp2='A';
                    break;
                }

            if(temp==temp2)
            {
                result=temp;
                printf("%c won\n",result);
                return 1;
            }
        }
    }

    return 0;
}

int check_horizntl(char arr[5][5])
{
    char result,temp,temp2;
    int t,i,l,k;

    for(k=0;k<4;k++)
    {
        temp=arr[k][0];

        if(temp!='.')
        {
            if(temp=='T')
                temp=arr[k][1];

            if(temp!='.')
            {
                temp2=temp;

                for(l=0;l<4;l++)
                {
                    if((arr[k][l]!=temp)&&(arr[k][l]!='T'))
                    {
                        temp2='A';
                        break;
                    }
                }

                if(temp==temp2)
                {
                    result=temp;
                    printf("%c won\n",result);
                    return 1;
                }
            }
        }
    }

    return 0;
}

int check_vertical(char arr[5][5])
{
    char result,temp,temp2;
    int t,i,l,k;

    for(k=0;k<4;k++)
    {
        temp=arr[0][k];

        if(temp!='.')
        {
            if(temp=='T')
                temp=arr[1][k];

            if(temp!='.')
            {

                temp2=temp;

                for(l=0;l<4;l++)
                {
                    if((arr[l][k]!=temp)&&(arr[l][k]!='T'))
                    {
                        temp2='A';
                        break;
                    }
                }

                if(temp==temp2)
                {
                    result=temp;
                    printf("%c won\n",result);
                    return 1;
                }
            }
        }
    }

    return 0;
}


int main(int argc, const char *argv[])
{
	string inputFileName = "A-large.in";
	string outputFileName = "output.out";
	freopen(inputFileName.c_str(), "r", stdin);
	freopen(outputFileName.c_str(), "w", stdout);

    char arr[5][5];
    char result,temp,temp2;
    int t,i,l,k,x;

    scanf("%d",&t);

    for(i=1;i<=t;i++)
    {
        for(k=0;k<4;k++)
            scanf("%s",arr[k]);

        printf("Case #%d: ",i);

        result='D';

        for(k=0;k<4;k++)
            for(l=0;l<4;l++)
            {
                if(arr[k][l]=='.')
                {
                    result='C';
                    break;
                }
            }

        x=check_angle(arr);

        if(x!=1)
            x=check_angle2(arr);

        if(x!=1)
            x=check_horizntl(arr);

        if(x!=1)
            x=check_vertical(arr);

        if(x!=1)
        {
            if(result=='C')
                printf("Game has not completed\n");

            else if(result=='D')
                printf("Draw\n");
        }
    }

    return 0;
}
