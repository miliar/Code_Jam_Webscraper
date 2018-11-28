#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("codejam2.out", "w", stdout);
    int testcases,y;
    cin>>testcases;
    for(y=1;y<=testcases;y++)
    {
        char s[101];
        int i,count=0;
        cin>>s;
        for(i=0;i<strlen(s);i++)
        {
            if(i==0&&s[i]=='-')
                count++;
            if(s[i]=='+')
            {
                while(s[i+1]=='-')
                    i++;
                if(s[i]!='+'&&(s[i+1]=='+'||s[i+1]=='\0'))
                    count=count+2;
            }
        }
        cout<<"Case #"<<y<<": "<<count<<endl;
    }
}
