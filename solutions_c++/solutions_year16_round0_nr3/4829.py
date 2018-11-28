#include <iostream>
#include <cmath>
#include <stdio.h>
using namespace std;

long long int divisor(long long int n)
{
    long long int j;
    /*if(n%2==0)
        return 2;
    if(n%3==0)
        return 3;
    j=5;
    while(1)
    {
        if(n%j==0)
            return j;
        if(n%(j+2)==0)
            return j;
        j+=6;
    }*/
    for(j=2;j<n;j++)
        if(n%j==0)
            return j;
}

bool primegen(long long int i)
{
    long long int j;
        if(i%2==0 || i%3==0)
           return false;
        else
        {
            j=5;
            while(j*j<=i)
            {
                if(i%j==0 || i%(j+2)==0)
                    return false;
                j+=6;
            }
            return true;
        }
}

long long int workd2b(long long int nums,int base)
{
    long long int i=0,pos=0,rem,j=1;
    while(nums!=0)
    {
        rem=nums%base;
        i+=rem*j;
        j*=10;
        nums/=base;
    }
    return i;
}

long long int workb2d(long long int nums,int base)
{
    long long int ans=0,i=1,rem;
    while(nums!=0)
    {
        rem=nums%10;
        nums/=10;
        ans+=rem*i;
        i*=base;
    }
    return ans;
}

int main()
{
    int j,k,l,flag,flag1,counter=0;
    long long int fir,baseans,i;
    //cout<<workd2b(111,3)<<endl;
    //cout<<workb2d(1000000001111011,3);
    FILE *fp;
    fp=fopen("ansofcoinjam.txt","w");
    fprintf(fp,"Case #1:\n");
    for(i=32769;i<=65535;i=i+2)
    {
        flag=0;
        fir=workd2b(i,2); //binary
        for(j=2;j<=10;j++)
        {
            baseans=workb2d(fir,j);
            if(primegen(baseans))
            {
                flag=1; //prime
                break;
            }
        }
        if(flag==0)
        {
            fprintf(fp,"%lld ",fir);
            for(j=2;j<=10;j++)
            {
                k=2;
                baseans=workb2d(fir,j);
                fprintf(fp,"%d ",divisor(baseans));
                //cout<<divisor(baseans)<<" ";
            }
            fprintf(fp,"\n");
            counter++;
            if(counter==50)
                break;
        }
    }
    return 0;
}
