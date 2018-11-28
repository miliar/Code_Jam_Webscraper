#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        string a;
        cin>>a;
        long s=0,p=0;
        if(a[0]=='-')
        {
            while(a[p]!='\0' && a[p]=='-')
            p++;
            s=1;
        }
        while(a[p]!='\0')
        {
            if(a[p]=='-')
            {
                while(a[p]!='\0' && a[p]=='-')
                p++;
                s+=2;
            }
            else
            {
                while(a[p]!='\0' && a[p]=='+')
                p++;
            }
        }
        cout<<"Case #"<<i<<": "<<s<<endl;
    }
    return 0;
}