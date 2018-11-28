#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>
using namespace std;
int main()
{
    int i,j,n,t,N,k;
    double s1,s2,c,f,x,d;
    freopen("B-large.in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    N=t;
    while(t--)
    {
        cin>>c>>f>>x;
        s1=0;
        s2=0;
        for(i=0;1;i++)
        {
            if(x/(2+f*i)<=x/(2+f*(i+1))+c/(2+f*i))
                break;
        }
        for(j=0;j<i;j++)
        {
            s1+=c/(2+j*f);
        }
        s1+=x/(2+i*f);
        printf("Case #%d: %.7lf\n",N-t,s1);
    }
    return 0;
}