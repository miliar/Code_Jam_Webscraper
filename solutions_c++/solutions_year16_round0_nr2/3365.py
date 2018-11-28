#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main() {
       
    long long int t,a[105],b[105],i,len,ans,count=0;
    string s;
    cin>>t;

    while(t--)
    {
        count++;
        cin>>s;
        for(i=0;i<105;i++)
            a[i]=b[i]=0;

        len=s.length();

        if(s[0]=='+')
        {
            a[0]=0;
            b[0]=1;
        }
        else
        {
            a[0]=1;
            b[0]=0;
        }

        for(i=1;i<len;i++)
        {
            if(s[i]=='+')
            {
                a[i]=min(a[i-1],b[i-1]+1);
                b[i]=min(a[i-1]+1,b[i-1]+2);
            }

            if(s[i]=='-')
            {
                a[i]=min(a[i-1]+2,b[i-1]+1);
                b[i]=min(a[i-1]+1,b[i-1]);
            }
        }

        ans=min(a[len-1],b[len-1]+1);

        cout<<"Case #"<<count<<": "<<ans<<endl;

    }

    return 0;
}
