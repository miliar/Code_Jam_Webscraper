#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;
int main()
{
    int T;
    cin>>T;
    int SMax;
    string s;
    int pplNeed,pplStand;
    int k=0;
    int out[T];
    int Size=T;
    while(T>0)
   {
       pplNeed=0;
    cin>>SMax;
    cin>>s;

    pplStand=s[0];
    pplStand-=48;

    for (int i=1;i<s.length();i++)
    {
       if(s.length()!=1)
        {
       REPEAT:
           if(i<=pplStand)
           {
               pplStand += s[i];
               pplStand-=48;
           }
       else
       {
        pplNeed++;
        pplStand++;
        goto REPEAT;
       }
        }
    }
    out[k]=pplNeed;
    k++;
   T--;
   }
   for(int j=0;j<Size;j++)
   {
       cout<<"Case #"<<j+1<<": "<<out[j]<<endl;
   }
}
