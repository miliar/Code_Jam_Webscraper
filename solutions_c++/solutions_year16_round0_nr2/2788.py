#include<bits/stdc++.h>
using namespace std;

char str[1000];
int f[1000][2];

int main()
{
    freopen("B-l.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    scanf("%d",&T);str[0]=1;
    for(int tcnt=1;tcnt<=T;tcnt++)
    {
        scanf("%s",str+1);
        int n=strlen(str)-1;
        f[0][0]=f[0][1]=0;
        for(int i=1;i<=n;i++)
        {
            int p=i;
            for(;p>0&&str[p]==str[i];p--);
            if(str[i]=='+')
            {
                f[i][0]=f[p][1]+1;
                f[i][1]=f[i-1][1];
            }
            else
            {
                f[i][1]=f[p][0]+1;
                f[i][0]=f[i-1][0];
            }
        }
        printf("Case #%d: %d\n",tcnt,f[n][1]);
    }
    return 0;
}
