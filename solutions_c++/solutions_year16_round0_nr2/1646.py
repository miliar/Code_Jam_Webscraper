#include<iostream>
#include<set>
#include<algorithm>
#include<string.h>
using namespace std;


int main()
{
    int i,j,k,z,x,y;
    int test;
    char str[1000];
    cin>>test;
    int ind=0;
    while(test--)
    {
        ind++;
        cin>>str;
        int ans=0;
        if(str[0]=='+')
            k=1;
        else
            k=0;
        i=0;
        x=strlen(str);
        if(k==0)
        {
            for(i=0;i<x;i++)
            {
                if(str[i]=='-')
                {
                    continue;
                }
                else
                    break;
            }
            ans=ans+1;
        }
        for(;i<x;i++)
        {
            z=0;
            while(str[i]=='+' && i<x)
                i++;
            while(str[i]=='-' && i<x)
               {
                   i++;
                   z=1;
               }
               if(z==1)
                ans=ans+2;
        }
        cout<<"Case #"<<ind<<": "<<ans<<endl;
    }
}
