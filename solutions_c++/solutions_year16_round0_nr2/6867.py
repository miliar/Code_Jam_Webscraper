#include <cstring>
#include <string>
#include <iostream>
using namespace std;
int main()
{
   int N,T;
   cin>>T;
   string str;
   char c;
   int i,t;
   for(t=1;t<=T;t++)
   {
        cin>> str;
        c = '.';
        int count = 0;
        for(i=0;i<str.length();i++)
        {
            if(str[i]!=c)
            {
                c =str[i];
                count++;
            }
        }
        if(c=='+')
            count--;
        cout<<"Case #"<<t<<": "<<count<<endl;
   }
    return 0;
}