#include <iostream>
#include <sstream>
#include <string>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

int main()
{
    int t,cas=1;
    int i;
    cin>>t;
    while(t!=0)
    {
        long int num1,num,val=0;
        int j=2,task=0;
        cin>>num;
        num1=num;
        bool visited[10];
       for(i=0;i<10;i++)
       {
           visited[i]=false;
       }
       if(num==0)
       {
          printf("Case #%d: INSOMNIA",cas);
          cout<<"\n";
          cas++;
          t--;
       }
       else
       {
       while(task<10)
       {

          while(num!=0)
          {
              val=num%10;
              num=num/10;
              if(visited[val]==false)
              {
              visited[val]=true;
              task++;
              }
          }
       long int b=num1;
       b=b*j;
       num=b;
       j++;
       }
       cout<<"Case #"<<cas<<": "<<num-num1<<"\n";
          cas++;

          t--;
       }

    }
    return 0;
}

