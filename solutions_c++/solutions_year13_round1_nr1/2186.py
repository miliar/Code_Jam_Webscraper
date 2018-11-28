#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>

using namespace std;

int main(int argc, const char *argv[])
{
	string inputFileName = "A-small-attempt0.in";
	string outputFileName = "output.out";
	freopen(inputFileName.c_str(), "r", stdin);
	freopen(outputFileName.c_str(), "w", stdout);

    long long r,t,n,i,x;
    long double a,b,c,z1,z2,tmp;

    //scanf("%lld",&n);
    cin>>n;

    for(i=1;i<=n;i++)
    {
        //scanf("%lld %lld",&r,&t);
        cin>>r>>t;

        a=2;
        b=1-(2*r);
        c=-t;

        tmp=b*b-4*a*c;
        tmp=sqrtl(tmp);

        z1=(b+tmp)/4;
        z2=(b-tmp)/4;

        z1=floorl(z1);
        z2=floorl(z2);

        if(z1>0)
            x=(long long)z1;

        else
            x=(long long)z2;

        printf("Case #%lld: %lld\n",i,x);
    }

    return 0;
}
