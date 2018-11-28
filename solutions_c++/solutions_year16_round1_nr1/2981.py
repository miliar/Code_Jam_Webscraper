#include<iostream>
#include<stdio.h>
#include<string>
using namespace std;
int main()
{
  freopen("A-large.in","r",stdin);
  freopen("a.txt","w",stdout);
  int i,cases,t;
  string input,tmp1,tmp2,answer;
  cin>>t;
  for(cases=1;cases<=t;cases++)
  {
    cin>>input;
    answer="";
    for(i=0;i!=input.size();i++)
    {
      tmp1=input.substr(i,1)+answer;
      tmp2=answer+input.substr(i,1);
      if(tmp1>=tmp2)
        answer=tmp1;
      else
        answer=tmp2;
    }
    printf("Case #%d: ", cases);
    cout<<answer<<endl;
  }
  return 0;
}