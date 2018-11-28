#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small-attempt2.out","w",stdout);
    int t;
    cin>>t;
    for(int q=0;q<t;q++)
    {
       int num1,num2,a[5][5],b[5][5],flag=0,counter=0,d=0;
       cin>>num1;
       for(int j=0;j<4;j++)
       {
           for(int l=0;l<4;l++)
           {
               cin>>a[j][l];
           }
       }
       cin>>num2;
       for(int j=0;j<4;j++)
       {
           for(int l=0;l<4;l++)
           {
               cin>>b[j][l];
           }
       }
        for(int i=0;i<4;i++)
       {
           for(int j=0;j<4;j++)
           {
               if(a[num1-1][i]==b[num2-1][j])
               {
                   flag=1;
                   counter++;
                   d=a[num1-1][i];
               }
           }
       }
       if(counter>1)
       {
           cout<<"Case #"<<q+1<<": Bad magician!\n";
       }
       else if(counter==1)
       {
           cout<<"Case #"<<q+1<<": "<<d<<"\n";
       }
       else
       {
           cout<<"Case #"<<q+1<<": Volunteer cheated!\n";
       }
    }

   return 0;
}
