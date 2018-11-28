#include<cstdio>
#include<iostream>
#include<fstream.h>
using namespace std;

int a[1011];
char s[1011];
int main()
{
    ofstream myfile;
  myfile.open ("so.txt");
  int i,t,ms,ans;
  cin>>t;
  for(i=1;i<=t;i++)
  {
                   ans=0;
              cin>>ms;
              cin>>s;     
              for(int j=0;j<=ms;j++)
              {
                      a[j]=(int)s[j]-48;
              }
             // cout<<a[ms]<<endl;
              for(int j=1;j<=ms;j++)
              {
                      if(a[j-1]<j)
                      {
                                  ans+=j-a[j-1];
                                  a[j-1]=j;
                      }
                      a[j]+=a[j-1];
              }
              myfile<<"Case #"<<i<<": ";
              
              myfile<<ans<<endl;
  }
  return 0;
}
