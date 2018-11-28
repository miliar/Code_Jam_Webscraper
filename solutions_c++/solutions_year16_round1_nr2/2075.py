#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int t,t1=1,i,pos,miss,j,miss2,temp,n;
    int v[100][50],ans[50];
    int done[100];
    cin>>t;
    while(t1<=t)
    {
      cin>>n;
      for(i=0;i<2*n-1;i++)
      {
          for(j=0;j<n;j++)
          {
             cin>>temp;
             v[i][j]=temp;
          }
      }
      for(i=0;i<2*n;i++)
      {
        done[i]=-1;
      }
      for(i=0;i<n;i++)
      {
         temp=1000000;
         for(j=0;j<2*n-1;j++)
         {
           if(done[j]==-1 && temp>=v[j][i])
           {
             temp=v[j][i];
           }
         }
         int flag=0;
         for(j=0;j<2*n-1;j++)
         {
           if(v[j][i]==temp)
           {
             done[j]=i;
             flag++;
           }
         }
         if(flag==1)
         {
           miss=i;
         }
      }
      //cout<<"miss= "<<miss<<endl;
      for(i=0;i<2*n-1;i++)
      {
        if(done[i]==miss)
        {
          miss2=i;
        }
      }
      ans[miss]=v[miss2][miss];
      for(i=0;i<n;i++)
      {
        int ans1=-1,ans2=-1,flag=0;
        if(i!=miss)
        {
          for(j=0;j<2*n-1;j++)
          {
            if(i==done[j])
            {
              flag++;
              if(flag==1)
              {
                ans1=v[j][miss];
              }
              if(flag==2)
              {
                ans2=v[j][miss];
              }
            }
          }
          if(ans1==v[miss2][i])
          {
            ans[i]=ans2;
          }
          else
          {
            ans[i]=ans1;
          }
          //cout<<ans1<<"--- "<<ans2<<endl;
        }
      }

      cout<<"Case #"<<t1<<": ";
      for(i=0;i<n;i++)
      {
        cout<<ans[i]<<" ";
      }
      cout<<endl;
      t1++;
    }
    return 0;
}
