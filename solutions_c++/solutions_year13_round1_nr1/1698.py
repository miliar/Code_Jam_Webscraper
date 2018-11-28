#include<iostream>
#include<sstream>
#include<cstdio>
#include<climits>
#include<cstring>
#include<map>
#include<set>
#include<cstdlib>
#include<cstdio>
#include<sstream>
#include<cmath>
#include<vector>
#include <algorithm> 
#include <sstream>

using namespace std;

int main()
{
int T,j;
cin>>T;
for(j=0;j<T;j++)
{
    long long int r,t,i=1,a,b,count=0,sum=0;
    cin>>r>>t;

    while(1)
    {  a=r*r;
       r=r+1;
       b=(r)*(r);
       sum=b-a;
       t=t-sum;
       if(t>=0)
       {  count++;}
       else break;
       r=r+1;
    } 
    cout<<"Case #"<<j+1<<": "<<count<<"\n";
  }
  // system("pause");
}




