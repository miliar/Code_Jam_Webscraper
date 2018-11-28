#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm> 
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
    int t,cas;
    double a,b,c;
    scanf("%d",&t); 
    for(cas=1;cas<=t;cas++){
        cin>>a>>b>>c;
        double r=c*0.5,A=0,F=0;
        while(A<r){
            A+=a/(2.0+F);
            double tmp=A+c*1.0/(2+F+b);
            F+=(double)b;
            r=min(r,tmp);
        }
        printf("Case #%d: %.8f\n",cas,r);
    }
    return 0;
}

