#include <iostream>
using namespace std;

int main()
{
	// your code goes here;
 int test,l=1;
 cin>>test;
 while(test)
 {
 int smax,s,i,q,t,ct=0,per=0;
 
 cin>>smax;
 char a[smax+2];
 cin>>a;
 //ct+=a[0]-'0';

 for(i=0;i<=smax;i++)
  {   t=a[i]-'0';
  
      if(ct>=i)
       { ct+=t;
         continue; }
      else
      {
          q=i-ct;
          ct=ct+q+t;
          per+=q;
      }
      
  }
 cout<<"case #"<<l<<": "<<per<<endl;
 l++;
 test--;
 } 
	return 0;
}