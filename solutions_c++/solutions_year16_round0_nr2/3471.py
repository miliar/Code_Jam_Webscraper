#include<cstdio>
#include<cstring>
using namespace std;
int n,cate;
char s[150];
int main()
{
    freopen("input","r",stdin);
    freopen("output","w",stdout);
    int Q;
    scanf("%d\n",&Q);
    for(int test=1;test<=Q;test++)
    {
        printf("Case #%d: ",test);
        gets(s+1);
        n=strlen(s+1);
        ///greedy
        cate=1;
        for(int i=2;i<=n;i++)
            if(s[i]!=s[i-1])cate++;
        if(s[n]=='+')cate--;
        printf("%d\n",cate);
    }
    return 0;
}
