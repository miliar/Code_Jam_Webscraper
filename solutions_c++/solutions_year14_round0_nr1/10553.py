#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<vector>

using namespace std;

int main()
{
   freopen("A-small-attempt1.in","r",stdin);
    freopen("output.txt","w",stdout);

   int test;
   cin>>test;

   for ( int testcases=1 ; testcases<=test ; testcases++ )
   {
       int a[17];
       for ( int i=0 ; i<17 ; i++ )
       {
          a[i]=0;
       }
       int n,temp;
       cin>>n;
       for ( int i=0 ; i<4 ; i++ )
       {

           for ( int j=0 ; j<4 ; j++ )
           {
               cin>>temp;
               if(i==n-1)
               a[temp]=1;
           }

       }
       cin>>n;
       int cnt=0,pos;
        for ( int i=0 ; i<4 ; i++ )
       {

           for ( int j=0 ; j<4 ; j++ )
           {
               cin>>temp;
               if(i==n-1)
               if(a[temp]==1)
               {
                cnt++;
                pos=temp;
               }
           }

       }
    if(cnt==1)
    {
        cout<<"\nCase #"<<testcases<<": "<<pos;
    }
    else if(cnt>1)
    {
        cout<<"\nCase #"<<testcases<<": "<<"Bad magician!";
    }
    else
        cout<<"\nCase #"<<testcases<<": "<<"Volunteer cheated!";

   }
    return 0;
}
