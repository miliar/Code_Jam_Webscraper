#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

int T,N,J,k=0;
long long val[11],fact[11];
long long getFactor(long long n){
    if(n>2 && (n%2)==0)
        return 2;
    for(long long i = 3; i*i <= n; i+=2)
        if((n%i)==0)
            return i;
    return 0;
}
void dfs(int depth){
    if(k==J)    return;
    if(depth == N){
        for(int i = 2; i <= 10; i++){
            fact[i] = getFactor(val[i]);
            if(!fact[i])    return;
        }
        printf("%lld ",val[10]);
        for(int i = 2; i <= 10; i++){
            printf("%lld ",fact[i]);
        }
        printf("\n");
        k++;
        return;
    }

    for(long long i = 2; i <= 10; i++)
        val[i]*=i;

    if(depth!=N-1){
        dfs(depth+1);
    }

    for(long long i = 2; i <= 10; i++)
        val[i]++;

    dfs(depth+1);

    for(long long i = 2; i <= 10; i++){
        val[i]--;
        val[i]/=i;
    }
}

int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    scanf("%d",&T);
    scanf("%d%d",&N,&J);
    for(int i = 2; i <= 10; i++)
        val[i] = 1LL;
    k = 0;
    printf("Case #1:\n");
    dfs(1);
    //cout<<"k="<<k;
    return 0;
}
