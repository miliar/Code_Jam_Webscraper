#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string.h>
using namespace std;
int mass[100][100];
int n,m;
int check(int x,int y, int val){
  bool f = true;
  for(int i = 0; i < n; i ++){
    if(mass[i][x] > val){
      f = false;
      break;
    }
  }
  bool f2 = true;
  for(int i = 0; i < m; i ++){
    if(mass[y][i] > val){
      f2 = false;
    }
  }
  if(!f && !f2){
    return -1;
  }
  if(f)
    return 0;
  return 1;
}


int solve(){
  set<int> all;
  for(int i = 0; i < n;i ++){
    for(int j = 0;j < m; j ++){
      all.insert(mass[i][j]*100*100+i*100+j);
    }
  }
  while(!all.empty()){
    int cur = *all.begin();
    int x = cur%100;
    cur/= 100;
    int y = cur%100;
    cur /= 100;
    int val = cur;
    int cans = check(x,y,val);
    if(cans == -1){
      return -1;
    }
    if(cans == 0){
      for(int i = 0; i < n; i ++){
        int tmp= mass[i][x]*100*100+i*100+x;
        all.erase(tmp);
      }
    }else{
      for(int i = 0;i < m;i ++){
        int tmp = mass[y][i]*10000+y*100+i;
        all.erase(tmp);
      }
    }

  }
  return 1;

}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    for(int qwe=0;qwe < t; qwe++){
      cin >> n >> m;
      for(int i = 0;i < n; i ++){
        for(int j = 0; j < m; j ++){
          scanf("%d",&mass[i][j]);
          mass[i][j] --;
        }
      }
      int ans = solve();
        printf("%s%d","Case #",qwe+1);
        if(ans == -1){
          printf("%s",": NO\n");
        }else{
          printf("%s",": YES\n");
        }
    }
}
