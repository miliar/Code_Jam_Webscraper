#include <iostream>
#include<stdio.h>
#define LL long long int

using namespace std;

FILE *ip,*op;
int main()
{
    int T;
    ip=fopen("in.txt","r");
    op=fopen("out.txt","w");
    fscanf(ip,"%d",&T);
    for(int z=1;z<=T;z++)
    {
        LL t,r,ans=0;
        fscanf(ip,"%lld %lld",&r,&t);

        for(LL i=2*r+1;i<=t;i+=4)
        {

            t-=i;
            ans++;


        }

        fprintf(op,"Case #%d: %lld\n",z,ans );
    }

    return 0;
}
