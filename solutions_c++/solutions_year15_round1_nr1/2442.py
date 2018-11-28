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
int maxx(int a, int b) {
  if(a<b) return b;
  return a;
}
int minn(int a, int b) {
  if(a<b) return a;
  return b;
}
int main(){
  int T;
  cin>>T;
  for(int cas = 1; cas <= T; ++ cas) {
    int n;
    cin>>n;
    int first;
    cin>>first;
    int sum = first;
    int ans1 = 0;
    int tt[2000];
    tt[0] = first;
    int max = 0;
    for(int i=1; i<n; ++i) {
      int cake;
      cin>>cake;
      max = maxx(max, first - cake);
      tt[i] = cake;
      if(i==n-1)
        sum-=cake;
      else
        sum+=cake;
      if(cake < first)
        ans1 += first - cake;
      first = cake;
    }
    int ans2 = 0;
    int cur = 0;
    //printf("max = %d", max);
    for(int i=0; i<n-1; ++i) {
      int cnt = minn(max, tt[i]);
      ans2 += cnt;
      cur -= cnt;
    }
    printf("Case #%d: %d %d\n", cas, ans1, ans2);
  }	
	return 0;
}
