#include<stdio.h>
#include<iostream>
using namespace std;
 
int main()
{
    long long int t,cases,r,p,out,count,rad1,rad2;
        cin>>t;
        for(cases=0;cases<t;cases++)
        {
                out = count = 0;
                cin>>r>>p;
                rad1=r;
                rad2=r+1;
                for(;out<=p;)
                {
                        count++;
                        out += rad2*rad2-rad1*rad1;
                        rad1 = rad2 + 1;
                        rad2 = rad1 + 1;                        
                }
                printf("Case #%lld: %lld\n",cases+1,count-1);
        }
        return 0;
}
