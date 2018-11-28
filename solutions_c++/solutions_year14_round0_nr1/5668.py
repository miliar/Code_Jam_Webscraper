#include<iostream>
using namespace std;
int main()
{
   int T,a1,a2,m1[4][4],m2[4][4],res,ans;
   int i,j,k,l;

   cin>>T;

   res=0;
   for(i=0;i<T;i++)
   {
     res=0;
     cin>>a1;
     for(j=0;j<4;j++)
     for(k=0;k<4;k++)
     cin>>m1[j][k];
     cin>>a2;
     for(j=0;j<4;j++)
     for(k=0;k<4;k++)
     cin>>m2[j][k];


     for(k=0;k<4;k++)
     for(j=0;j<4;j++)
     if(m1[a1-1][k]==m2[a2-1][j])
      {
      res+=1;
      ans=m1[a1-1][k];
      }

      if(res==1)
       cout<<"Case #"<<i+1<<": "<<ans<<"\n";
      else
      if(res>1)
       cout<<"Case #"<<i+1<<": Bad magician!\n";
      else
       cout<<"Case #"<<i+1<<": Volunteer cheated!\n";

   }
return 0;
}
