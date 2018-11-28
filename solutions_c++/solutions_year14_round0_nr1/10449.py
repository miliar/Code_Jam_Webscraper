#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int t,test,i,j,k,count=0,temp=0,val=0,try1,try2;
     cin >>test;
    int inp[4];
    for(t = 0; t < test; t++) {
      cin>>try1;
        for(i=0;i<4;i++)
          {
              if(i==try1-1)
                {
                for(j=0;j<4;j++)
                  {
                  cin>>inp[j];

                }

              }
              else
                {
                  for(j=0;j<4;j++)
                    {
                  cin>>temp;
                  }
              }
   
        }
      
      cin>>try2;
      for(i=0;i<4;i++)
          {
          if(i==try2-1)
            {
                for(j=0;j<4;j++)
                  {
                    cin>>temp;
                    for(k=0;k<4;k++)
                    {
                      if(temp==inp[k])
                      {count++;val=temp;}

                     }

            }
          }
          else
            {
           		for(j=0;j<4;j++)
                    {
                  cin>>temp;
                  }
          }
   
        }
      if(count==1)
        cout<<"Case #"<<t+1<<": "<<val<<"\n";
      else if(count==0)
        cout<<"Case #"<<t+1<<": "<<"Volunteer cheated!\n";
        else if(count>1)
      cout<<"Case #"<<t+1<<": "<<"Bad magician!\n";
        count=0;temp=0;
      
    }
    
    return 0;
}
