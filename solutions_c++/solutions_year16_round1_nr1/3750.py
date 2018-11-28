#include<stdio.h>
#include<string>
#include<iostream>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    int i,t,co=1;
    string s,w;
    cin>>t;
    while(t--)
    {
        cin>>s;
        w=s[0];
        for(i=1;s[i]!=0;i++)
        {
            if(s[i]>=w[0])
            {
                w=s[i]+w;
            }
            else
                w=w+s[i];
        }
        printf("Case #%d: ",co++);
        cout<<w<<endl;
    }
    return 0;
}
