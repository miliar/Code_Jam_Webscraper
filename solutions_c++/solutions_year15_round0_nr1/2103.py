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
int main(){
  int T;
  cin>>T;
  char in[2000];
  for(int i=0; i<T; ++i) {
    int ma;
    cin>>ma;
    cin>>in;
    int ans = 0;
    int cnt = 0;
    for(int j=0; j<=ma; ++j){
      int diff;
      if(cnt < j)
        diff = j - cnt;
      else
        diff = 0;
      ans += diff;
      cnt += in[j] -'0' + diff;

    }
    printf("Case #%d: %d\n", i+1, ans);
  }
    
	return 0;
}
