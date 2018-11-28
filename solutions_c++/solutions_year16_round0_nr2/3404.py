#include<cstdio>
#include<cstring>
using namespace std;
char a[111];
void solve()
{
    int sz;
    int answer=0;
    sz=strlen(a);
    for(int i=1;i<sz;i++)
        if(a[i]=='-'&&a[i]!=a[i-1])answer+=2;
    if(a[0]=='-')answer++;
    printf("%d\n",answer);
}
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        scanf("%s",a);
        printf("Case #%d: ",i);
        solve();
    }
}
