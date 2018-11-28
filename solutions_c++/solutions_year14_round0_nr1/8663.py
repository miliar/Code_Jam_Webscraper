#include<iostream>
using namespace std;
int main()
{
    int t,c=0;
    cin>>t;
    while(t--)
    {
              c++;
              int ans1;
              cin>>ans1;
              int a[4],p,seen[4],b[4];
              for(int i=0;i<4;i++)
              {
                      seen[i]=0;
                      for(int j=0;j<4;j++)
                      {
                              cin>>p;
                              if(i+1==ans1)
                              a[j]=p;
                      }
              }
              cin>>ans1;
              for(int i=0;i<4;i++)
              {
                      for(int j=0;j<4;j++)
                      {
                              cin>>p;
                              if(i+1==ans1)
                              {
                                           b[j]=p;
                              }
                      }
              }
              int cnt=0,ind=-1;
              for(int i=0;i<4;i++)
              {
                      for(int j=0;j<4;j++)
                      {
                              if(b[i]==a[j])
                              {
                                            seen[i]=1;
                                            ind=i;
                                            cnt++;
                                            break;
                              }
                      }
              }
              cout<<"Case #"<<c<<": ";
              if(cnt>1)
              cout<<"Bad magician!"<<endl;
              else if(cnt==0)
              cout<<"Volunteer cheated!"<<endl;
              else
              cout<<b[ind]<<endl;
              
    }
}
