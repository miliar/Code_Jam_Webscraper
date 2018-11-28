#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("tl1.in","r",stdin);
    freopen("tl2.txt","w",stdout);
 int t;
 cin>>t;
 for(int i=1;i<=t;i++)
 {
  int n;
  cin>>n;

  int a[10];
  for(int c=0;c<10;c++) a[c]=0;

  if(n==0)
   printf("Case #%d: INSOMNIA\n",i);
  else
   {
     for(int j=1;j<=200;j++)
     {
       int k=n*j;
       // cout<<k<<" ";
       int num=k;
       while(k>0)
       {
        a[k%10]=1;
        k=k/10;
       }

       int fl=0;
       for(int h=0;h<10;h++)
       {
           if(a[h]==0)
            fl=1;
       }
       if(fl==0){printf("Case #%d: %d\n",i,num);break;}
     }
   }
 }
return 0;
}
