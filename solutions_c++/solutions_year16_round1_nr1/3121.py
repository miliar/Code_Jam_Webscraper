#include <iostream>
#include <string.h>
#include <stdio.h>
typedef long long ll;
using namespace std;
FILE *f1=freopen("input.in","rt",stdin);
FILE *f2=freopen("output.ou","wt",stdout);
void output(char s[])
{
    char s1[2005];
    ll fron=1002, rear=fron;
    s1[fron]=s[0];
    for (ll i=1;i<strlen(s);i++)
        if (s[i]>=s1[fron]) s1[--fron]=s[i];
        else s1[++rear]=s[i];
    for (ll i=fron;i<=rear;i++) cout<<s1[i];
}
int main()
{
    ll t,c;
    char s[1002];
    scanf("%I64d%*c",&t);
    for (c=0;c<t;c++)
    {
        gets(s);
        cout<<"Case #"<<c+1<<": ";
        output(s);
        cout<<endl;
    }
    return 0;
}
