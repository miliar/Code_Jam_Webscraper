#include<bits/stdc++.h>
#define MAX 105
using namespace std;
string s;
int sol(int n)
{
    if(n==0) return (s[0]=='+')?0:1;
    while(n>=0 && s[n]=='+') n--;
    if(n<0) return 0;
    if(n==0) return 1;
    if(s[n-1]=='-')
        return sol(n-1);
    else
        return 2+sol(n-1);
}
int main()
{
    int test;
    scanf("%d", &test);
    for(int te=1;te<=test;te++)
    {
        cin>>s;
        printf("Case #%d: %d\n", te, sol(s.size()-1));
    }
}

