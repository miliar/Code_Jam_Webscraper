#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int T;
long long calc(int n)
{
    int tab[10],cnt=0;
    memset(tab,0,sizeof(tab));
    long long now=n,temp;
    for(int i=1;;i++){
        temp=now*i;
        while(temp){
            if(tab[temp%10]==0){
                tab[temp%10]=1;++cnt;
            }
            temp/=10;
        }
        if(cnt==10)
            return now*i;
    }
}
int main()
{
    //freopen("A-small-attempt0","r",stdin);
    freopen("data.out","w",stdout);

    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++){
        int n;
        scanf("%d",&n);
        if(n)
            printf("Case #%d: %lld\n",kase,calc(n));
        else
            printf("Case #%d: INSOMNIA\n",kase);
    }

    return 0;
}
