#include<bits/stdc++.h>
using namespace std;
int main()
{
       int T,it,i,j,N,x,d;

       freopen("A-large.in","r",stdin);
       freopen("A.out","w",stdout);
       scanf("%d",&T);
       for(it=1; it<=T; it++)
       {
             scanf("%d",&N);
             if(N==0){
                printf("Case #%d: INSOMNIA\n",it);
                continue;
             }

             set<int>u;
             u.clear();

             for(i=1; i<=100; i++)
             {
                   x = i*N;
                   while(x>0){
                         d = x%10;
                         u.insert(d);
                         x/=10;
                   }
                   if(u.size()==10){
                         printf("Case #%d: %d\n",it,i*N);
                         break;
                   }
             }


       }
       return 0;
}
