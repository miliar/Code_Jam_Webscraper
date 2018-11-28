#include<bits/stdc++.h>
using namespace std;
bool ch[12];
int check(int x)
{
    for(int i=1;x>0;i++)
    {
        ch[x%10]=true;
        x/=10;
    }
    int ans=0;
    for(int i=0;i<=9;i++) ans+=ch[i];
    return ans==10;
}
int solve(int n)
{
    int i;
    if(n==0) return -1;
    if(n%10==0) return ch[0]=true,solve(n/10);
    for(i=1;;i++)
    if(check(i*n)) break;
    return i;
}
int main()
{
    int n,t;
    freopen("test.inp","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        memset(ch,0,sizeof ch);
        scanf("%d",&n);
        int tmp=solve(n);
        printf("Case #%d: ",i);
        if(tmp<0) printf("INSOMNIA\n");
        else
        printf("%d\n",tmp*n);
    }
}
