#include<iostream>
#include<algorithm>
using namespace std;


long long int a1[1000100];
int main()
{
    freopen("A-large (3).in","r",stdin);
    freopen("osmosout4.in","w",stdout);
    long long int t,i,n,am,k=1;
    cin>>t;
    while(t--)
    {
              long long int sum=0,count=0,f=1,j,cal;
              cin>>am>>n;
              for(i=0;i<n;i++)
                              cin>>a1[i];
              sort(a1,a1+n);
   //           for(i=0;i<n;i++)
    //            cout<<a1[i]<<endl;
 long long int min=n;
              if(am==1)
              {
                                count=n;                      
                                cout<<"Case #"<<k++<<": "<<count<<endl;
              }
              
              else
              {
                 
                       sum=am;
                       for(i=0;i<n;i++)
                       {
                  //                     cout<<"second"<<endl;
                                j=(n-i-1); 
                                  while(sum<=a1[i])
                                  {
                                                   
                                            // cout<<"38"<<;
                                                sum=sum+(sum-1);
                                                count++;
                                  }
                                  cal=count+j;
                                  if(cal<min) min=cal;
                                  sum+=a1[i];
                       }
                       // if(count>j) count=j;                                         
              cout<<"Case #"<<k++<<": "<<min<<endl;
              }         
             // cout<<"count ="<<count<<"  j="<<j<<endl;
    }
    return 0;
}

