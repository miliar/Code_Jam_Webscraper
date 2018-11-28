#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    long int t,i;
    cin>>t;
    for(i=1;i<=t;i++)
    {
    double c,f,x,mi,r=2,d=0,s;
    long int j;
    cin>>c>>f>>x;
    mi=x/2;
    for(j=1;j<(int)x;j++)
    {
       d+=c/r;
        r+=f;
        s=d+x/r;
        if(s<=mi)
            mi=s;
        else
            break;
    }
    cout<<"Case #"<<i<<": ";
    printf("%.7f",mi);
    }
    return 0;
}
