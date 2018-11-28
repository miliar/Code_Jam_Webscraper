#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
    int a1[4], a2[4];
    int cases,row,n,count=1,flag = 0;
    cin>>cases;
    while(cases--)
    {
          cout<<"Case #"<<count<<": ";
          count++;
          cin>>row;
          for(int i=0;i<4;i++)
          {
                  for(int j=0;j<4;j++)
                  {
                          if(i == (row-1))
                          {
                               cin>>a1[j];
                              // cout<<a1[j]<<" ";
                          }
                          else
                              cin>>n;
                          
                  }
          }
          cin>>row;
          for(int i=0;i<4;i++)
          {
                  for(int j=0;j<4;j++)
                  {
                          if(i == (row-1))
                          {
                               cin>>a2[j];
                              // cout<<a2[j]<<" ";
                          }
                          else
                              cin>>n;
                          
                  }
          }
          flag = 0;
          for(int i=0;i<4;i++)
          {
                  for(int j=0;j<4;j++)
                  {
                          if(a1[i]==a2[j] && !flag)
                          {
                               flag = 1;
                               n = a1[i];
                          }
                          else if(a1[i]==a2[j] && flag)
                          {
                               cout<<"Bad magician!\n";
                               flag = 2;
                               break;
                          }
                  }
                  if(flag == 2)
                     break;
          }
          if(flag == 1)
          {
                  cout<<n<<endl;
          }
          else if(flag == 0)
               cout<<"Volunteer cheated!\n";
    }
    return 0;
}
