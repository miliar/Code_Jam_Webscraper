#include <iostream>
#include <iostream>
#include<cstdlib>
#include<stdlib.h>
#include<stdio.h>
using namespace std;

int main()
{

   freopen("B-small-attempt0.in", "r+", stdin);
	freopen("abcde.txt", "w+", stdout);
    //int a=5 & 7;
    //cout<<a;
    long t,a,b,j,k,i,m;
    long long z,cc=0;
    cin>>t;
    for(i=0;i<t;i++)
    {
      cin>>a>>b>>k;
      cc=0;
      for(j=0;j<a;j++)
      {
          for(m=0;m<b;m++)
          {
                z=j & m;
                if(z<k)
                   cc++;
               // else
                 //   goto qwe;
          }
      }
   // qwe:;
    cout<<"Case #"<<i+1<<": "<<cc<<'\n';
    }



    return 0;
}
