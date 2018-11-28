#include<iostream>
#include<string.h>
#include<string>
#include<cstring>
using namespace std;
int main()
{
    int t,t1;
    cin>>t;
    t1=t;
    while(t--)
    {
        char a[101];
        cin>>a;
        int len=strlen(a);
        int calci=0;
        for (int i=0;i<len;i++)
        {
            if (a[0]=='-')
            {
                while(a[i]=='-')
                {
                    a[i]='+';
                    i++;
                }
                calci++;
            }
            else if (a[i]=='-')
            {
                while(a[i]=='-')
                    i++;
                calci+=2;
            }
        }
        cout<<"Case #"<<t1-t<<": "<<calci<<endl;
    }
}
