#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<iostream>
using namespace std;
void print(double x)
{
    int a=floor(x);
    cout<<a<<".";
    x-=a;
    for(int i=0;i<8;++i)
    {
        x*=10;
        a=floor(x);
        x-=a;
        cout<<a;
    }
    cout<<"\n";
}
int main()
{
    freopen("E:\\in.c","r",stdin);
    freopen("E:\\out","w",stdout);
    double x,f,c;
    int i,j,t,n;
    cin>>t;
    for(int tc=1;tc<=t;++tc)
    {
        cout<<"Case #"<<tc<<": ";
        //scanf("%f %f%f",&c,&f,&x);
        cin>>c>>f>>x;
        if(c>=x)
           {
               print(x/2.0);
               continue;
           }
           double klimit=x/c-2/f;
           if(klimit<2)
            klimit=2;
           double mi=x/2.0;
           double sum=0;
           for(i=1;i<=klimit;++i)
           {
               sum+=c/(2+(i-1)*f);
               double ne=sum+x/(2+i*f);
               if(ne<mi)
               {
                   mi=ne;
               }
           }
           print(mi);
    }
}
