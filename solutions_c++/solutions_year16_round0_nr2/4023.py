#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<algorithm>
using namespace std;
char s[105];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("resB.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++)
    {
        scanf("%s",s);
        int n=strlen(s);
        int res=(s[n-1]=='-');
        for(int i=1;i<n;i++)
            res+=(s[i]!=s[i-1]);
        printf("Case #%d: %d\n",ca,res);
    }
    return 0;
}
