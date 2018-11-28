#include <iostream>
#include<bits/stdc++.h>
#include<cassert>
#include<string>
using namespace std;

int main()
{
    FILE *fin = freopen("B-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("B-large.out", "w", stdout);

    int t;
    char s[105];
    char c;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int co=0;
        int ans=1;
        scanf("%s",s);

        if(strlen(s)==1 && s[0]=='-')
        {
            cout << "Case #" << i << ": " <<1<< endl;
            continue;
        }
        else if(strlen(s)==1 && s[0]=='+')
        {
            cout << "Case #" << i << ": " <<0<< endl;
            continue;
        }
        c=s[0];
        for(int k=1;s[k]!='\0';k++)
        {
            if(c!=s[k])
            {
                c=s[k];
                co++;
            }
        }
        if((co==0 && s[0]=='+') || (s[0]=='-' && co==1))
        {
                if(co==0)
                {
                    cout << "Case #" << i << ": " <<0<< endl;
                }
                else if(co==1)
                {
                    cout << "Case #" << i << ": " <<1<< endl;
                }
        }
        else
        {
        c=s[0];
        for(int j=1;s[j]!='\0';j++)
        {
            if(c!=s[j])
            {
                c=s[j];
                ans++;
            }
        }
        if(s[strlen(s)-1]=='-')
        cout << "Case #" << i << ": " <<ans<< endl;
        else if(s[strlen(s)-1]=='+')
        cout << "Case #" << i << ": " <<(ans-1)<< endl;

        }
    }
    return 0;
}
