#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#include <list>
#include <fstream>
#include<string.h>
#define MAX 3050
using namespace std;

int main()
{
      ifstream cin ("B-large.in");
      ofstream cout ("output.txt");
      int t,r=1;
      cin>>t;
      while(t--)
      {
            cout<<"Case #"<<r++<<": ";
           int n,m;
           cin>>n>>m;
           int arr[n][m];
           for(int i=0;i<n;i++)
           {
            for(int j=0;j<m;j++)
            {
                  cin>>arr[i][j];
            }
           }
           int flag=0;
           int ans[n][m];
           for(int i=0;i<n;i++)
           {
                  int ma=0;
                  for(int j=0;j<m;j++)
                  ma=max(ma,arr[i][j]);
                  for(int j=0;j<m;j++)
                  ans[i][j]=ma;
           }
         //  cout<<n<<" dsdsd  "<<m<<endl;
         
           for(int i=0;i<m && flag==0;i++)
           {
                 // cout<<"DSDS    "<<i<<endl;
                 int hi=-1,low=-1;
                  for(int j=0;j<n && flag==0;j++)
                  {
                  //cout<<arr[j][i]<<"  ";
                        if(arr[j][i]!=ans[j][i])
                        {
                              if(hi==-1 && low==-1)
                              hi=arr[j][i];
                              else if(hi==-1 && low!=-1)
                              {
                                    if(arr[j][i]<low)
                                    flag=1;
                                    else
                                    hi=arr[j][i];
                              }
                              else if(hi!=-1 && arr[j][i]!=hi)
                              flag=1;
                        }
                        else if(arr[j][i]==ans[j][i])
                        {
                              if(hi==-1 && low==-1)
                                    low=ans[j][i];
                              else if(hi==-1)
                                    low=max(ans[j][i],low);
                              else if(arr[j][i]>hi)
                              flag=1;
                              else 
                              low=max(ans[j][i],low);
                        }
                  }
                  //cout<<endl;
            }
            if(flag==0)
            cout<<"YES"<<endl;
            else
            cout<<"NO"<<endl;
      }
      return 0;
}
