#include <iostream>
#include<cstdio>

using namespace std;

int main()
{
   int T,z;
   scanf("%d",&T);
   for(z=1;z<=T;z++)
   {
       int a1,a2,i,ans=0,cnt=0,x,j;
       int arr1[17]={0};
       int arr2[17]={0};
       scanf("%d",&a1);
       for(i=0;i<4;i++)
       {
           for(j=0;j<4;j++)
           {
               scanf("%d",&x);
               if((i+1)==a1)
               arr1[x]=1;
           }
       }


       scanf("%d",&a2);
       for(i=0;i<4;i++)
       {
           for(j=0;j<4;j++)
           {
               scanf("%d",&x);
               if((i+1)==a2)
               arr2[x]=1;
           }
       }

       for(i=0;i<17;i++)
       {
           if(arr1[i] && arr2[i])
           {
                cnt++;
                ans=i;
           }
       }
       if(cnt==1)
       cout<<"Case #"<<z<<": "<<ans;
       if(cnt>1)
       cout<<"Case #"<<z<<": "<<"Bad magician!";
       if(cnt==0)
       cout<<"Case #"<<z<<": "<<"Volunteer cheated!";
       cout<<endl;
   }

   return 0;
}
