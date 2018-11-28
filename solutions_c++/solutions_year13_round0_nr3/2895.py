#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
using namespace std;
long long a[100]={1,4,9,121,484,12321,14641,44944,1234321,123454321,125686521};
main()
{
      int i1,t,i,o;
      long long c1,c2,e;
      freopen("C-small-attempt0.in","r",stdin);
      freopen("C-small-attempt0.out","w",stdout);
      
      e=111111;
      a[11]=e*e;
      e=1111111;
      a[12]=e*e;
      e=11111111;
      a[13]=e*e;
      e=111111111;
      a[14]=e*e;
      cin>>t;
      for(i1=1;i1<=t;i1++)
      {
                          scanf("%lld %lld",&c1,&c2);
                          //cout<<"num is"<<c1<<" "<<c2<<endl;
                          o=0;
                          for(i=0;i<=14;i++)
                          {
                                           if(c1<=a[i]&&a[i]<=c2)o++;
                          }
                          printf("Case #%d: %d\n",i1,o);
      }
}
