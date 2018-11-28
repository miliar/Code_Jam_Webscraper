#include <iostream>
 
using namespace std;
int main(){
    long long int T,j, N,h, ans,flag,count1,k;
count1=0;
    cin>>T;
 while(T--)
 {flag=0;
     count1++;
      cin>>N;
      j=N;
 
 if(N==0)
      {cout<<"Case #"<<count1<<": INSOMNIA"<<endl;
      continue;
      }
       int count[10]={0};
      while(1)
      {flag=0;
          h=N;
          while(N>0)
          {
             k=N%10;
             if(count[k]==0)
             count[k]=1;
             N=N/10;
          }
          for(int i=0;i<10;i++)
          {
              if(count[i]==0)
                flag=1;
          }
 
          if(flag==0)
          {cout<<"Case #"<<count1<<": "<<h<<endl;
          break;
 
          }
          N=h+j;
      }
 
 
 }
     return 0;
 }
 
 