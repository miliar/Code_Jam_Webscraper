#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAX_NUM		150

int  checkPossible(int Value[100][100],int i,int j,int N,int M)
{
     int flag=0;
     for(int m=0;m<N;m++)
     {
        if(Value[i][j]<Value[m][j])
        {
          flag+=1;
          break;
        }     
     }
     
     for(int m=0;m<M;m++)
     {
        if(Value[i][j]<Value[i][m])
        {
          flag+=1;
          break;
        }             
     }
     if(flag==2)
      return 0;
      else
      return 1;
}           



int main() {
//freopen("B-large.in","r",stdin);
// freopen("key.txt","w",stdout);
int T=0,N,M;
cin>>T;
	double begin;
    double end;
    int Value[100][100];
for(int i=1;i<=T;i++)
{
        int lowest=100;
        int largest=0;
        int flag=0;
        cin>>N>>M;
        for(int i=0;i<N;i++)
           for(int j=0;j<M;j++)
           {
                   cin>>Value[i][j];
                   if(Value[i][j]<lowest)
                        lowest=Value[i][j];
                    if(Value[i][j]>largest)
                        largest=Value[i][j];

           }

        for(int i=0;i<N&&flag==0;i++)
          {
              for(int j=0;j<M;j++)  
              {
                  if(checkPossible(Value,i,j,N,M)==0)
                   {
                      flag=1;                               
                      break;
                   }  
                           
              }      
          }        
        if(flag==1)
        cout<<"Case #"<<i<<": "<<"NO"<<endl;
        else
        {
             cout<<"Case #"<<i<<": "<<"YES"<<endl;
        }
}
  return 0;
}
