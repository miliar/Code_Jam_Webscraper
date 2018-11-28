#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<math.h>
using namespace std;
long long int chartoi(char *p,int N,int base)
{
    long long int val=0,mul=1;
    int i=0,j=N-1;
    while(j>=0)
    {
        val=val + (p[j] - '0')*mul;
        j--;
        i++;
        mul=mul*base;
    }
    //printf("%lld\n", val);
    return val;
}
void next (char *p,int N)
{
    int i;
    i=N-2;
    while(i>0)
    {
        if(p[i]=='1')
        {
            p[i]='0';
        }
        else if(p[i]=='0')
        {
            p[i]='1';
            break;
        }
        i--;
    }
}
bool isprime(long long int B,long long int *m)
{
    int k;
    for(k=2;k<=sqrt(B);k++)
    {
        if(B%k==0)
        {
            *m=k;
            return false;
        }
    }
    *m=-1;
    return true;
}
int main()
{
    long long int T,N,J,i,j,A[20],M[20];
    bool trynext;
    int k,base;
    char str[100],tmp[100];
    scanf("%lld", &T);
    scanf("%lld%lld", &N,&J);
    printf("Case #1:\n");
    for(i=0;i<N;i++)
        str[i]='0';
    str[0]='1';
    str[N-1]='1';
    str[N]='\0';
    for(j=0;j<J;)
    {
        trynext=false;
        for(k=2;k<=10;k++)
        {
            A[k]=chartoi(str,N,k);
            trynext=isprime(A[k],&M[k]);
    //        printf("%lld is divisible by %lld\n", A[k],M[k]);
            if(trynext)
            {
                break;
            }
        }
        if(!trynext)
        {
            printf("%s ", str);
            for(k=2;k<=10;k++)
            {
                printf("%lld ", M[k]);
            }
            printf("\n");
            j++;
        }
        next(str,N);
    }
}
