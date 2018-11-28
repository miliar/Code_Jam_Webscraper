#include<bits/stdc++.h>
using namespace std;
int cnt[30];
int N;

int findmax()
{
     int id=-1,i;
     for(i=0; i<N; i++){
          if(cnt[i]==0)  continue;
          if(id==-1||cnt[i]>cnt[id])
              id=i;
     }
     return id;
}

int main()
{
     int T,it,i,j;
     freopen("A-large.in","r",stdin);
     freopen("A.out","w",stdout);
     scanf("%d",&T);
     for(it=1; it<=T; it++)
     {
         scanf("%d",&N);
         int tot=0;
         for(i=0; i<N; i++) {

                scanf("%d",&cnt[i]);
                tot+=cnt[i];
         }

         printf("Case #%d:",it);
         int now = N;

         while(tot>0){

              int mx = findmax();
              printf(" %c",mx+'A');
              cnt[mx]--;
              tot--;
              if(tot==0)  break;

              int mx1 = findmax();
              if(cnt[mx1] > tot-cnt[mx1]){
                  printf("%c",mx1+'A');
                  tot--;
                  cnt[mx1]--;
              }

         }

         puts("");

     }
     return 0;
}
