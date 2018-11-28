#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#define ll long long int

using namespace std;

int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("AS1.txt","w",stdout);
    // std::ios_base::sync_with_stdio(false);
    int t,cases=1,i;
    cin>>t;
    while(t--)
    {
        string s;
        int j=0;
        char stch='\0',str[1050];
        memset(str,'\0',sizeof(str));
        cin>>s;
        stch=s[0];
        str[j] = stch;
        char ch;
        for(i=1;i<s.length();i++)
        {
            if(s[i]>=stch)
            {
                for(j=strlen(str);j>=1;j--)
                {
                    str[j] = str[j-1];
                }
                str[j]=s[i];
                stch = s[i];
            }
            else
            {
                str[strlen(str)] = s[i];
            }
        }
        cout<<"Case #"<<cases<<": ";
        for(j=0;j<s.length();j++)
        {
            cout<<str[j];
        }
        cout<<endl;
        s.clear();
        cases++;


    }


    return 0;
}
