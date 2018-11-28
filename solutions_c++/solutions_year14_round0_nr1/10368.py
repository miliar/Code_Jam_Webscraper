#include <iostream>
#include <stdio.h>
#include <fstream>
using namespace std;

int main()
{

    freopen("A-small-attempt7.in","rt",stdin);
    freopen("please.out","wt",stdout);
    int t,ans1,ans2,arr1[4][4],arr2[4][4],a,i,j,scount,op;
    cin>>t;
    for(a=1;a<=t;a++)
    {scount=0;
     op=0;
     cin>>ans1;
     for(i=0;i<4;i++)
      for(j=0;j<4;j++)
       cin>>arr1[i][j];
     cin>>ans2;
     for(i=0;i<4;i++)
      for(j=0;j<4;j++)
       cin>>arr2[i][j];
     for(i=0;i<4;i++)
      for(j=0;j<4;j++)
       {
        if(arr1[ans1-1][i]==arr2[ans2-1][j])
        {
         scount++;
         if(scount==1)
         {
          op=arr1[ans1-1][i];
         }
        }
       }
     if(scount==0)
     {
      cout<<"Case #"<<a<<": Volunteer cheated!\n";
     }
     else if(scount==1)
     {
      cout<<"Case #"<<a<<": "<<op<<endl;
     }
     else
     {
      cout<<"Case #"<<a<<": Bad magician!\n";
     }
    }
    return 0;
}
