#include <fstream>
#include <iostream>
#include <string.h>
using namespace std;
char S[101];
int pan(int n)
{
    char str[n];
    int i,ans=0;
    for(i=0;i<n;i++)
        str[i]=S[i];
    i=0;
    if(str[0]=='+')
        ans=1;
    while(str[i]=='+')
    {
        str[i]='-';
        i++;
    }
    for(i=0;i<n;i++)
    {
        if(str[i]=='+')
            S[n-i-1]='-';
        else
            S[n-i-1]='+';
    }
    ans++;
    return ans;
}
int main()
{
    int t, n, i, c, ans=0;

    ofstream op;
    op.open("output.in");

    ifstream ip;
    ip.open("B-large.in");

    ip>>t;
    for(c=1;c<=t;c++)
    {
        ip >> S;
        n=strlen(S);
        ans=0;
        for(i=n-1;i>=0;i--)
        {
            if(S[i]=='-')
                ans = ans + pan(i+1);
        }
        op<<"Case #"<<c<<": "<<ans<<endl;
    }
    ip.close();
    op.close();
    return 0;
}
