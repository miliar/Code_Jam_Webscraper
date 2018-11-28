#include <iostream>
#include <string.h>
#include <stack>
#include <queue>
using namespace std;
char rev(char a)
{
    if(a=='-')
    return '+';
    else
    return '-';
}
int main()
{
    int t,it=1;

    cin>>t;
    while(it<=t)
    {
        char str[105];
        cin>>str;
        int flag=0;
        int len=strlen(str);
        int count=0;
        while(flag==0)
        {
            int temp=0;
            for(int i=0;i<len;i++)
            {
                if(str[i]=='+')
                temp++;
            }
            if(temp==len)
            {
                flag=1;
                cout<<"Case #"<<it<<": "<<count<<endl;
                break;
            }
            int i=0;
            char a;
            do
            {
                a=str[i];
                str[i]=rev(str[i]);
                i++;

                //cout<<"i a"<<endl;
            }
            while(a==str[i] && i<len);
            count++;
        }


        it++;
    }
}
