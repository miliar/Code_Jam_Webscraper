#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<cstring>
using namespace std;


int main()
{
    int t;
    cin>>t;
    for(int p=0;p<t;p++)
    {
    char ch[100];
    cin>>ch;
    int count=0;
        int i=0;
        int len=strlen(ch);
        
       while(i<len-1)
      {
         if(ch[i]=='+' && ch[i+1]=='-')
         {
             count+=2;
                int j=i+1;
             while(ch[j]=='-')
             {ch[j]='+';j++;}
             i=j-1;
         }
          if(ch[i]=='-'&& ch[i+1]=='+')
         {
             count++;
             i++;
              
         }
         
         if(ch[i]==ch[i+1])
           i++;
       }
        if(count ==0 && ch[0]=='-')
            count=1;
      cout<<"Case #"<<p+1<<":"<<" "<<count<<endl;
    }
    return 0;
}
