#include<cstdio>
#include<iostream>
#include<fstream.h>
using namespace std;

int main()
{
    ofstream myfile;
  myfile.open ("oo.txt");
  int i,t,x,r,c,ans;
  cin>>t;
  for(i=1;i<=t;i++)
  {

              cin>>x>>r>>c;
              
              myfile<<"Case #"<<i<<": ";
              ans=r*c;
              if(ans%x==0 && ans>=(x*(x-1)))
              myfile<<"GABRIEL"<<endl;
              else
              myfile<<"RICHARD"<<endl;
  }
  return 0;
}
