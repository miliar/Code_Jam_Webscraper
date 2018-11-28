#include<stdio.h>
#include<iostream>
#include<set>
#include<algorithm>
#define mod(x) x%1000000007
#include<cstring>
#include<vector>
#include<math.h>
#include <stdlib.h>
using namespace std;

char findsymbol(int rot,char ch)
{
    if(ch=='+' && rot%2==0)
        return '+';
    else if(ch=='+' && rot%2!=0)
        return '-';
    else if(ch=='-' && rot%2!=0)
        return '+';
    else
        return '-';
}

int main(){
    int t;
    cin>>t;
    for(int tt=0;tt<t;tt++)
    {
       int k,c,s;
       cin>>k>>c>>s;
       cout<<"Case #"<<tt+1<<": ";
       if(c==1 || k==1)
       {
          if(s>=k)
              for(int i=1;i<=k;i++)
                  cout<<i<<" ";
           else
                  cout<<"IMPOSSIBLE";
       }
       else
       {
           if(s>=k-1)
              for(int i=2;i<=k;i++)
                  cout<<i<<" ";
           else
             cout<<"IMPOSSIBLE";
       }
       cout<<endl;
    }
    }

