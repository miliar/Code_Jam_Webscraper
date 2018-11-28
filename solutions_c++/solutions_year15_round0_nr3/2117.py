#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<set>
#include<queue>
#include<list>
#include<vector>
#define LL long long
#define INF 0x7fffffff
#define For(i,a,b) for(int i=a; i<b; ++i)
using namespace std;
typedef pair<int,int> ii;
int mymap[5][5] = {{0,1,2,3,4}
                ,{0,1,2,3,4}
                ,{0,2,-1,4,-3}
                ,{0,3,-4,-1,2}
                ,{0,4,3,-2,-1}
                };
int convert(char c) {
  if(c=='i') return 2;
  if(c=='j') return 3;
  return 4;
}
int mul(int a, int b) {
  if(a<0) return -mul(-a,b);
  if(b<0) return -mul(a,-b);
  return mymap[a][b];
}
int main(){
  int T;
  cin>>T;
  for(int cas = 1; cas <=T; ++cas){
    LL L, X;
    cin>>L>>X;
    char str[10002];
    cin>>str;
    int state = 0;
    LL total = L * X;
    int cur = 0;
    for(int i=0; i<total; ++i){
      cur = mul(cur, convert(str[i%L]));
      if(state == 0 && cur == 2){
        state = 1;
        cur = 0;
      }
      else if(state == 1 && cur == 3){
        state = 2;
        cur = 0;
      }
    }
    
    if(state == 2 && cur == 4)
      printf("Case #%d: YES\n", cas);
    else
      printf("Case #%d: NO\n", cas);
  }  
	return 0;
}
