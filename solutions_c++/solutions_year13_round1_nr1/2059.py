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
int main(){
  int T;
  int r,t,cases=1;
  freopen("input.txt","r",stdin);
  freopen("output.out","w",stdout);
  scanf("%d",&T);
  while(T--){
    scanf("%d%d",&r,&t);
    int ans=0,k=r;
    while(t>0){
      ++k;
      int j=(k*k-(k-1)*(k-1));
      if(t>=j) ++ans,t-=j;
      else break;
      ++k;
     }
     printf("Case #%d: %d\n",cases++,ans);
  }
  return 0;
}
