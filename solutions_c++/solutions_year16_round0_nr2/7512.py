#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main()
{
    int T,i,j,count,n;
    char s[101];
    cin>>T;
    for(i=0;i<T;i++)
    {
        scanf("%s",s);
        n=strlen(s);
        count = 0;
        if(n==1)
        {
            if(s[0]=='+')
                cout<<"Case #"<<i+1<<": 0"<<endl;
            else
                cout<<"Case #"<<i+1<<": 1"<<endl;
            continue;
        }
        for(j=0;j<n-1;j++)
            if(s[j]!=s[j+1])
                count++;
        if(s[0]=='+'&&count!=0&&s[n-1]=='-')
            count++;
        else if (s[n-1]=='-')
            count++;
        cout<<"Case #"<<i+1<<": "<<count<<endl;
    }
    return 0;
}
