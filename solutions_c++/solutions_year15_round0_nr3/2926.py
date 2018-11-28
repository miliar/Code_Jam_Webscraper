#include <bits/stdc++.h>
using namespace std;

const int I=0x02;
const int J=0x03;
const int K=0x04;

int  mlt[5][5]={
  {0,0,0,0,0},
  {0,1,I,J,K},
  {0,I,-1,K,-J},
  {0,J,-K,-1,I},
  {0,K,J,-I,-1}
};

int  l,x,r;
int  dp[10001][5];
char s[10001];

int num(char c) {
  return c-'i'+2;
}

void dfs(int x,int c) {
  if (x==l) {
    r=c==0;
    return;
  }
  if (!c)
    return;
  if (dp[x][c]==-1) {
    dp[x][c]=1;
    int p=1;
    for (int i=x;!r&&i<=l;i++) {
      if (p==c) {
        if (c==J)
          dfs(i,K);
        else if (c==K)
          dfs(i,0);
      }
      if (i==l)
        break;
      int sig=p<0;
      p=mlt[abs(p)][num(s[i])];
      if (sig)
        p=-p;
    }
  }
}

int main(void) {
  int t;
  scanf("%d",&t);
  for (int cs=1;cs<=t;cs++) {
    scanf("%d%d\n",&l,&x);
    scanf("%s",s);
    for (int i=1,j=l;i<x;i++,j+=l)
      memcpy(s+j,s,l);
    l*=x;
    r=0;
    memset(dp,0xff,sizeof dp);
    int p=1;
    for (int i=0;!r&&i<=l;i++) {
      if (p==I)
        dfs(i,J);
      if (i==l)
        break;
      int sig=p<0;
      p=mlt[abs(p)][num(s[i])];
      if (sig)
        p=-p;
    }
    printf("Case #%d: ",cs);
    r? puts("YES"):puts("NO");
  }
}
