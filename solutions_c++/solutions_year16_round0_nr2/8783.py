#include<bits/stdc++.h>
using namespace std;
char x[105];
int dp[105][2], tab[105];
int main(){
  int test;
  scanf("%d",&test);
  for(int t=1;t<=test;t++){
    scanf(" %s", x+1);
    for(int i=1;x[i];i++) {
      if(x[i]=='+') tab[i]=1;
      else tab[i]=0;
    }
    dp[1][0]=tab[1];
    dp[1][1]=1-tab[1];
    int n=1;
    for(int i=2;x[i];i++){
      dp[i][tab[i]]=dp[i-1][tab[i]];
      dp[i][1-tab[i]]=dp[i-1][tab[i]]+1;
      n=i;
    }
    printf("Case #%d: %d\n", t, dp[n][1]);
  }  
}