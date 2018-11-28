#include <iostream>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
using namespace std;
long long M=1000000007;
int main()
{
    int t,k=1,sum,j,temp;
    cin>>t;
    while(t>0)
    {
                   cout<<"Case #"<<k<<": ";
              int n,i;
              cin>>n;
              sum=0;
              int a[n+1],b[n+1];
              for(i=0;i<n;++i)
              {
                              cin>>a[i];
                              sum=sum+a[i];
                              b[i]=i;
                              
              }
              while(sum>0)
              {
                          if(n>2)
                          {
                          for(i=0;i<n;++i)
                          for(j=0;j<n-1-i;++j)
                          {
                                          if(a[j]>a[j+1])
                                          {
                                                         temp=a[j];
                                                         a[j]=a[j+1];
                                                         a[j+1]=temp;
                                                         temp=b[j];
                                                         b[j]=b[j+1];
                                                         b[j+1]=temp;
                                          }
                          }
                          if(a[n-3]>0 && a[n-3]>(sum-2)/2)
                          {
                                      cout<<char(65+b[n-1])<<" ";
                                      --a[n-1];
                                      sum=sum-1;
                          }
                          else if(a[n-2]>0)
                          {
                               cout<<char(65+b[n-1])<<char(65+b[n-2])<<" ";
                                      --a[n-1],--a[n-2];
                                      sum=sum-2;
                           }
                           else
                           {
                                      cout<<char(65+b[n-1])<<" ";
                                      --a[n-1];
                                      sum=sum-1;
                          }
                          }
                          else
                          {
                              cout<<char(65)<<char(66)<<" ";
                              sum=sum-2;
                              }
                              }
    --t;     
    ++k;     
    cout<<endl;
    }
    cin>>t;
    return 0;
}
