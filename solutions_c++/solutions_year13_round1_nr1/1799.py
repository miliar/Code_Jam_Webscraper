#include<map>
#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    FILE *fp=fopen("input.txt","r");
    FILE *fo=fopen("output.txt","w");
    long long int T,cases=1;
    long long int r,t;
    fscanf(fp,"%lld",&T);
    for(cases=1;cases<=T;cases++)
    {
        fscanf(fp,"%lld%lld",&r,&t);
        long long int paint_req=0;
        long long int i=1,cnt=0;
        bool done=false;
        for(;paint_req<=t&& !done;)
        {
            //printf("%lld\n",cnt);
            cnt++;
            paint_req+=(2*r + (i*i -((i-1)*(i-1))));
            if(paint_req>t)
            {
                done=true;
                cnt--;
                paint_req-=(2*r + (i*i -((i-1)*(i-1))));
                break;
            }
            i+=2;
        }
        fprintf(fo,"Case #%lld: %lld\n",cases,cnt);

    }
    return 0;
}

