# include<bits/stdc++.h>

using namespace std;

int main()
{
   int t,count,n,ac,i,j,cn;
   char st[1000],arr[1000];
   cin>>t;
   for(j=1;j<=t;j++)
   {
        memset(arr,0,1000);
        count=ac=0;
        cin>>n;
        cin>>st;
        arr[0]=st[0]-48;
        for(i=1;i<=n;i++)
          {
             arr[i]=arr[i-1]+st[i]-48;
          }     
        for(i=1;i<=n;i++)
          {
              if(arr[i-1]>=i)
                continue;
              else
                {
                    cn=i-arr[i-1];
                    count=count+cn;
                    for(ac=0;ac<=n;ac++)
                       arr[ac]=cn+arr[ac];
                }       
          }
        cout<<"Case #"<<j<<": "<<count<<endl;
  }
return 0;
}
