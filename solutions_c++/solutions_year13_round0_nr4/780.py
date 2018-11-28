#include <iostream>
#include <stdio.h>
#include <cstring>
using namespace std;
int kk,n;
int key[405];
int k[205],t[205];
int hak[205][405];
bool have[205];
int ans[205];
bool got;
bool steps[10000000];
int er[25];
void readin(){
  scanf("%d%d",&kk,&n);
  memset(key,0,sizeof(key));
  int temp;
  for (int i=0;i<kk;i++){
    scanf("%d",&temp);
    key[temp]++;
  }
  for (int i=1;i<=n;i++){
    scanf("%d%d",&t[i],&k[i]);
    for (int j=0;j<k[i];j++){
    scanf("%d",&hak[i][j]);
  }
  }
}
void work(int st,int zt){
  if (st==n) {got=true;return;}
  for (int i=1;i<=n;i++){
      if(got) return ;
    if (!have[i]&&key[t[i]]>0){
       int temp = zt+er[i-1];
       if (steps[temp]) continue;
       //cout <<temp<<endl;
       steps[temp]=true;
       key[t[i]]--;
       have[i]=true;
       for (int j=0;j<k[i];j++) key[hak[i][j]]++;
       ans[st]=i;
       work(st+1,temp);
      // ans[st]=0;
       have[i]=false;
       for (int j=0;j<k[i];j++) key[hak[i][j]]--;
       key[t[i]]++;
       if(got) return;
    }
  }
}
int main()
{
    freopen("D-small-attempt2.in","r",stdin);
    freopen("D-small-attempt2.out","w",stdout);
    int T,ca=1;
    scanf("%d",&T);
    er[0]=1;
    for (int i=1;i<=20;i++)er[i]=er[i-1]*2;
    while (T--){
      readin();
      memset(ans,0,sizeof(ans));
      memset(have,0,sizeof(have));
      memset(steps,0,sizeof(steps));
      got=false;
      work(0,0);
      printf("Case #%d:",ca++);
      if(got){
         for (int i=0;i<n;i++) printf(" %d",ans[i]);
      }
      else cout<<" IMPOSSIBLE";
      cout<<endl;
    }
    return 0;
}
