#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int N;
char ch[1100];
int main()
{
    freopen("inal.in","r",stdin);
    freopen("outal.out","w",stdout);
    int T;
    scanf("%d",&T);
    int tt = 0;
    while(T--)
    {tt++;
        scanf("%d",&N);
        scanf("%s",ch);
        int s = 0,ans = 0;
        for(int i=0;i<=N;i++)
        {
            if(s < i && ch[i] != '0')
            {
                ans += i-s;
                s = i;
            }
            s += ch[i] - '0';
        }
        printf("Case #%d: %d\n",tt,ans);
    }
    return 0;
}
