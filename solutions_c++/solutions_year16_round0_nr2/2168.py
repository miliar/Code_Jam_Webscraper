#include<cstdio>
#include<cstring>

using namespace std;

int n;
char str[110];

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);

    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        scanf("%s",str);
        int len=strlen(str);
        int ans=(str[len-1]=='-');
        for(int i=0;i<len-1;i++)
            if(str[i]!=str[i+1])
                ans++;
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
