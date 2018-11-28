//GCJ
/*
ID: Geek7
LANG: C++
TASK:
STATE:
MEMO:
*/
#include<iostream>
#include<cmath>
#include<map>
#include<cstring>
#include<cstdio>
#include<cstdarg>
#include<cstdio>
#include<cassert>
#include<vector>
#include<string>
#include<algorithm>
#include<list>
#include<set>
#include<queue>
#include<stack>
#include<sstream>
#include<numeric>
#include<functional>
#include<utility>
#include<bitset>
#define LL long long
#define maxab(a,b) (a)>(b)?(a):(b)
#define LL long long
using namespace std;
const int MAXN=110;
char maze[MAXN][MAXN],maze_[MAXN][MAXN],MM[MAXN],MM_[MAXN];
int m,n;
int main(){
  int T,cases=1;
  bool flag;
 // freopen("input.txt","r",stdin);
 // freopen("output.out","w",stdout);
  scanf("%d",&T);
  while(T--){
    scanf("%d%d",&m,&n);
    for(int i=0;i<m;++i){
      MM[i]=0;
      for(int j=0;j<n;++j){
        scanf("%d",&maze[i][j]);
        if(maze[i][j]>MM[i]) MM[i]=maze[i][j];
      }
    }
    for(int i=0;i<m;++i)
      for(int j=0;j<n;++j){
        maze_[i][j]=MM[i];
      }
    for(int i=0;i<n;++i){
      MM_[i]=101;
      for(int j=0;j<m;++j)
        if(maze_[j][i]!=maze[j][i] && maze[j][i]<MM_[i]) MM_[i]=maze[j][i];
    }
  /* for(int i=0;i<m;++i) printf("%d  ",MM[i]);
    printf("\n");
    for(int i=0;i<n;++i) printf("%d  ",MM_[i]);
    printf("\n");*/
  flag=1;
  for(int i=0;i<n;++i){
   if(MM_[i]!=101)
     for(int j=0;j<m;++j)
       if(MM_[i]<maze_[j][i]) maze_[j][i]=MM_[i];
  }
    for(int i=0;i<m;++i){
      for(int j=0;j<n;++j)
        if(maze[i][j]!=maze_[i][j]){
          flag=0;
          break;
        }
      if(!flag) break;
    }
    if(flag) printf("Case #%d: YES\n",cases++);
    else printf("Case #%d: NO\n",cases++);
  }
  return 0;
}
