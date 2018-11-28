#include<iostream>
#include<sstream>
#include<cstdio>
#include<climits>
#include<cstring>
#include<map>
#include<set>
#include<cstdio>
#include<cmath>
#include<vector>
#include <algorithm> 
using namespace std;
#define R return
#define FR(i,a,b) for(i=a;i<b;i++)
#define RFR(i,a,b) for(i=a;i>=b;i--)

typedef long long int ll;
int main()
{
int t,j;
cin>>t;
for(j=0;j<t;j++)
{      
    long long int c,d,i,count=0;
    cin>>c>>d;
    for(i=c;i<=d;i++)
        {
        long long int a=i,b,rev=0,digit;
        double s;
        bool flag1=false,flag2=false;
        b=a;
        while( b!=0)
        { digit=b%10;
          rev=rev*10+digit;
          b=b/10;
        }
        if(rev==a)
        flag1=true;
        //cout.precision(50);
        s = sqrt(a);
        if(s==ceil(s))
        {   b=(long long int)s;
            rev=0;
            while( b!=0)
            { digit=b%10;
              rev=rev*10+digit;
              b=b/10;
            }
          if(rev==s)
          { flag2=true;}
        }
        if(flag1==true &&flag2==true)
         { //cout<<a<<" "<<s<<"\n"; 
         count++;
         }
        }
     cout<<"Case #"<<j+1<<": "<<count<<"\n";
  }
  // system("pause");
}




