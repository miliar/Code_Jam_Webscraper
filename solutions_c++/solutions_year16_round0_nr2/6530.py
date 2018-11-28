#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    long long int T;
    string N;
    scanf("%lld",&T);
    for(int t=0;t<T;t++)
    {
        cin>>N;
        int len=N.length(),flip=1,cntp=0,cntn=0;
        char arr[len];
        for(int i=0;i<len;i++)
        {
            arr[i]=N.at(i);
            if(arr[i]=='+')
                cntp++;
            /*else
                cntn++;*/
        }
        for(int j=len-1;j>=0;j--)
        {
            if(arr[j]=='+')
                cntn++;
            else
                break;
        }
        len-=cntn;
        if(cntp==N.length())
        {
            cout<<"Case #"<<t+1<<": 0"<<endl;
            continue;
        }
        for(int j=len-1;j>=0;j--)
        {
            if(arr[j]=='+')
            {
                  for(int z=0;z<=j;z++)
                  {
                      if(arr[z]=='+') arr[z]='-';
                      else arr[z]='+';
                  }
                  flip++;
            }
        }
        cout<<"Case #"<<t+1<<": "<<flip<<endl;
    }
   return 0;
}

