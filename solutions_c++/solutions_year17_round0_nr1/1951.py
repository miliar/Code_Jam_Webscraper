#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int N;
char S[2000];
char ans[1000];

void solve(){
    //if all are + return 0
    int cnt = 0;
    int len = strlen(S);
    int i = 0;
    while(i+N <= len){
        if(S[i]=='+') {
            i++; continue;
        }

        for(int j=i; j<i+N; j++){
                S[j] = S[j]=='+'? '-' : '+';
        }
        cnt++;
        i++;
    }
    for(int j=len-1; j>=len-N; j--){
        if(S[j]=='-'){
            sprintf(ans,"IMPOSSIBLE");
            return;
        }
    }
    sprintf(ans,"%d",cnt);
}

int
main ()
{
  int T;
//freopen("input.txt","r",stdin);
  //  freopen("output.txt","w",stdout);
  scanf ("%d", &T);



  for(int t=1; t<=T; t++)
    {
      scanf("%s %d",S, &N);
      solve();
      printf ("Case #%d: %s\n",t, ans);
    }
  return 0;
}
