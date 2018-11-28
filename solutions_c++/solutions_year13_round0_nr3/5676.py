#include<iostream>
#include<cmath>

int p(long);

int main()
{
   using namespace std;
   int T;
   cin>>T;
   for(int i=0;i<T;i++){
      long double N,M;
      cin>>N;
      cin>>M;
      int C=0;
      for(long double j=N;j<=M;j++)
         if(p(j)==1&&p(sqrt(j))==1){ 
            long t=sqrt(j);
            if(t==sqrt(j)) C+=1;
            }
      cout<<"Case #"<<i+1<<": "<<C<<endl;
   }
   return 0;
}

int p(long n)
{
  long temp=n,m=0;
  while(temp!=0.0){
  m=m*10+temp%10;
  temp=temp/10;
  }
  if(m==n) return 1;
  else return 0;
}
