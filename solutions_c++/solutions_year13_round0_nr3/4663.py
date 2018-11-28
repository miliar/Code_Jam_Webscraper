#include<iostream>
#include<vector>
#include<string>
#include<cstdlib>
#include<cmath>
using namespace std;


bool findifpalin(long long A)
{
  int length=0;
  long long upper=A;
  while(A)
  {
    A/=10;
    length++;
  }
  
  while(length>1)
  {
    long long int t=pow(10,length-1);
    long long rem=upper%t;
    upper=(upper-rem)/t;
    int lower=rem%10;
    if(upper!=lower)
    {
      return false;
    }
    upper=(rem-lower)/10;
    length=length-2;
  }
  return true;
}
    

int getpalin(long long A, long long B)
{
  long long counter=0;
  for(long long int i=A;i<=B;i++)
  {
    if(findifpalin(i))
    {
      if(findifpalin(i*i))
      {
	counter++;
      }
    }
  }
  return counter;
}


int main()
{
  int T;
  cin>>T;
  vector<int> results(T,0);
  cin.ignore();
  for(int i=0;i<T;i++)
  {
    string temp;
    char *pend;
    getline(cin,temp);
    
    long long int A=strtoll(temp.c_str(),&pend,10);
    long long int B=strtoll(pend,NULL,10);
    long long int rootA=sqrt(A);    
    long long int rootB=sqrt(B);
    if((rootA*rootA)<A)
    {
      rootA++;
    }
    results[i]=getpalin(rootA,rootB);
  }
  for(int i=0;i<T;i++)
  {
    cout<<"Case #"<<i+1<<": "<<results[i]<<endl;
  }
}
