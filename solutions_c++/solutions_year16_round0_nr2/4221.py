#include<iostream>
#include<cstring>
#include<stdio.h>
#define SIZE 100
using namespace std;
int main()
{
  freopen("B-large.in","r",stdin);
  freopen("b.txt","w",stdout);
  char input[SIZE+1],tmp[SIZE+1];
  int length,i,j,cases,t,index,answer;
  cin>>t;
  for(cases=1;cases<=t;cases++)
  {
    printf("Case #%d: ", cases);
    cin>>input;
    answer=0;
    length=strlen(input);
    tmp[length]='\0';
    while(true)
    {
      for(i=0;i<length;i++)
      {
        if(input[i]=='-')
          break;
        input[i]='-';
      }
      if(i==length)
        break;
      if(i>0)
        answer++;
      for(i=0;i<length;i++)
      {
        if(input[i]=='+')
          break;
        input[i]='+';
      }
      answer++;
    }
    cout<<answer<<endl;
  }
}