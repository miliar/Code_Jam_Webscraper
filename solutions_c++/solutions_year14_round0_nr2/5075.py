#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
int t;
double r=2.0,c,f,x,ans[101],min,a,b;
cin>>t;
for(int k=0;k<t;k++)
{
    r=2.0;
//cin>>c>>f>>x;
scanf("%lf %lf %lf",&c,&f,&x);
min=x/r;
a=c/r;
r+=f;
b=x/r;
    while(min>(a+b))
    {
        min=(a+b);
        a+=c/r;
        r+=f;
        b=x/r;
        //cout<<a<<" "<<b<<endl;
    }
    ans[k]=min;
}
for(int k=0;k<t;k++)
{
    cout<<"Case #"<<k+1<<": ";//<<ans[k]<<endl;
    printf("%lf\n",ans[k]);
}
return 0;
}
