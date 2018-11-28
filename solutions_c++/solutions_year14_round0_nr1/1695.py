/*************************************************************************
    > File Name: a.cpp
    > Author: implus
    > Mail: 674592809@qq.com
    > Created Time: 六  4/12 11:16:09 2014
 ************************************************************************/

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<string>
#include<set>
#include<queue>
#include<stack>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define ls (rt<<1)
#define rs (rt<<1|1)
#define lson l,m,ls
#define rson m+1,r,rs
int T, r, icase = 1;
int a[5][5];

int main(){
  scanf("%d", &T);
  while(T--){
    scanf("%d", &r);r--;
    for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++) scanf("%d", &a[i][j]);
    set<int> s;
    for(int j = 0; j < 4; j++){
      s.insert(a[r][j]);
    }
    scanf("%d", &r);r--;
    for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++) scanf("%d", &a[i][j]);
    vector<int> v;
    for(int j = 0; j < 4; j++){
      if(s.count(a[r][j])) v.push_back(a[r][j]);
    }
    if(v.size() == 1){
      printf("Case #%d: %d\n", icase++, v[0]);
    }else if( v.size() == 0){
      printf("Case #%d: Volunteer cheated!\n", icase++);
    }else 
      printf("Case #%d: Bad magician!\n", icase++);
  }
  return 0;
}
