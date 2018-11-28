#include <iostream>

using namespace std;

int main()
{
  int t;
  int arr[1001],smax,sum=0,v=0,st,i=0,m;
  char a;
  cin>>t;
   m=t;
  while(t--)
  {
      sum=0;
      st=0;
      cin>>smax;
     
      cin>>a;
      sum=a-'0';
      i=1;
      while(smax--)
      {
          cin>>a;
          v=a-'0';
          if(sum<i)
          {
              st=st+i-sum;
              sum=sum+i-sum;
          }
          sum=sum+v;
          i++;
      }
      cout<<"Case #"<<m-t<<": "<<st<<endl;
  }
   
   return 0;
}

