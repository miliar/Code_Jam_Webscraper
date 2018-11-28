#include<iostream>
#include<stdio.h>

using namespace std;

int saperate(int n,int* digits)
{
    int index;
    int count=0;
    while(n>0)
    {
        index=n%10;
        if(digits[index]==0)
        {
            count=count+1;
            digits[index]=1;
        }
        n=n/10;
    }
    return count;
}

int main()
{
    int t;
    int n;
    int digits[10];
    int digit_count;
    int caseid=1;
    int original;


    FILE* input=fopen("D:\\Education\\codes\\Google Code Jam\\A-large.in","r");
    FILE* output=fopen("D:\\Education\\codes\\Google Code Jam\\output.in","w");

    fscanf(input," %d",&t);


    while(t--)
    {
        fscanf(input," %d",&n);
        original=n;
        digit_count=0;

        if(n==0)
        {
            fprintf(output,"Case #%d: INSOMNIA\n",caseid);
            caseid++;
            continue;
        }

        for(int i=0;i<10;i++)
        {
            digits[i]=0;
        }

        while(1)
        {
            digit_count=digit_count+saperate(n,digits);
            if(digit_count==10) break;
            n=n+original;
        }
        fprintf(output,"Case #%d: %d\n",caseid,n);
        caseid++;
    }
    printf("Completed\n");
    return 0;

}
