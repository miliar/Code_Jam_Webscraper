#include<iostream>
#include<cstdio>
#include<cstring>
#include<queue>
#include<cmath>

using namespace std;

int n;
int c;
char s[1005];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
    cin>>n;
    for(int i = 0;i<n;i++)
    {
        scanf("%d%s",&c,s);
        int pri = s[0]-'0';
        int ans = 0;
        for(int j = 1;j<strlen(s);j++)
        {
            if(pri<j) {
                    ans+= (j-pri);
                    pri = s[j]-'0' + j;
            }
            else pri = pri+s[j]-'0';
        }
        printf("Case #%d: %d\n",i+1,ans);
    }
    return 0;
}
