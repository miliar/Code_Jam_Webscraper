#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<set>
#include<queue>
#include<list>
#include<vector>
#include<algorithm>
#define LL long long
#define INF 0x7fffffff
#define For(i,a,b) for(int i=a; i<b; ++i)
#define min(a,b) (a)>(b)?(b):(a)
using namespace std;
typedef pair<int,int> ii;
int main(){
  int T;
  cin>>T;
  for(int i=0; i<T; ++i) {
    int D;
    cin>>D;
    int count[2000];
    for(int j=0; j<2000; j++){
      count[j] = 0;
    }
    int mini = 10001;

    for(int j=0; j<D; ++j){
      int temp;
      cin>>temp;
      count[temp]++;
    }
    
    for(int j=1; j<=1000; ++j){
      int cnt = 0;
      for(int k=1; k<=1000; ++k) {
        cnt += ((k+j-1)/j - 1) * count[k];
      }
      mini = min(mini, cnt+j);
    }
      
    
    printf("Case #%d: %d\n", i+1, mini);   
  }

	return 0;
}
