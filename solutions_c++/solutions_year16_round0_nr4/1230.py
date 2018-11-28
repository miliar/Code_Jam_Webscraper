#include<bits/stdc++.h>
using namespace std;
int main()
{
       int T,K,C,it,i,j,S;

       freopen("D-small-attempt0.in","r",stdin);
       freopen("D.out","w",stdout);
       scanf("%d",&T);
       for(it=1; it<=T; it++)
       {
              scanf("%d%d%d",&K,&C,&S);

              long long diff = 1LL;
              for(i=1; i<C; i++)
                  diff *= K;

              printf("Case #%d:",it);

              for(i=0; i<K; i++)
                  printf(" %lld",1LL+diff*i);

              puts("");
       }
       return 0;
}
