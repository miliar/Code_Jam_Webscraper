#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;


bool fun(long double a,long double b)
{
    return a>b;
}
bool check(long double ele,long double *b,int n)
{
    for(int i=0;i<n;i++)
        if(b[i]>ele && b[i]!=0)
    {
        b[i]=0;return true;
    }
return false;
}
bool check2(long double ele,long double *b,int n)
{
    for(int i=0;i<n;i++)
        if(b[i]>ele && b[i]!=0)
    {
        b[i]=0;return true;
    }
return false;
}

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("war.out","w",stdout);

    int t;
    cin>>t;

    for(int k=1;k<=t;k++)
    {

      int n;
      cin>>n;

     long double a[n],b[n],c[n],d[n];
     for(int i=0;i<n;i++)
        {cin>>a[i];c[i]=a[i];}
     for(int i=0;i<n;i++)
        {cin>>b[i];d[i]=b[i];}

     if(n==1)
     {
         if(a[0]>b[0])
         printf("Case #%d: 1 1\n",k);
         else
        printf("Case #%d: 0 0\n",k);
     }
     else
     {
        int c1=0,c2=0;


       sort(a,a+n);
       sort(b,b+n);
        //for(int i=0;i<n;i++) cout<<a[i]<<" ";cout<<endl;
        //for(int i=0;i<n;i++) cout<<b[i]<<" ";cout<<endl<<endl;
        for(int i=0;i<n;i++)
        {

             if(check(a[i],b,n))
                a[i]=0;
            else
                c2++;


        }
        /*for(int i=0;i<n;i++) cout<<a[i]<<" ";cout<<endl;
        for(int i=0;i<n;i++) cout<<b[i]<<" ";cout<<endl;*/
       sort(c,c+n);
       sort(d,d+n);

      /*for(int i=0;i<n;i++) cout<<c[i]<<" ";cout<<endl;
        for(int i=0;i<n;i++) cout<<d[i]<<" ";cout<<endl<<endl;*/


      for(int i=0;i<n;i++)
      {
          if(check2(d[i],c,n))
                d[i]=0;
            else
                c1++;

      }

      /*for(int i=0;i<n;i++) cout<<c[i]<<" ";cout<<endl;
        for(int i=0;i<n;i++) cout<<d[i]<<" ";cout<<endl;*/


      printf("Case #%d: %d %d\n",k,n-c1,c2);
     }




    }

return 0;
}
