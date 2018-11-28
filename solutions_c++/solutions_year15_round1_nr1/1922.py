#include <cstdio>
#include <algorithm>
using namespace std;

int T;
int N;
int M[1024];
int ans1, ans2;
int maxx, rate;
int now;

int main(){
  int i, j;

  scanf("%d", &T);
  for(int tt = 1; tt <= T; tt++){
    scanf("%d", &N);
    for(i = 0; i < N; i++)
      scanf("%d", &M[i]);

    ans1 = ans2 = 0;
    maxx = 0;

    for(i = 1; i < N; i++){
      if(M[i] < M[i - 1]){
	ans1 += M[i - 1] - M[i];
	
	if(maxx < M[i - 1] - M[i])
	  maxx = M[i - 1] - M[i];
      }
    }
    now = M[0];
    for(i = 1; i < N; i++){
      ans2 += min(now, maxx);
      now = M[i];
    }

    printf("Case #%d: %d %d\n", tt, ans1, ans2);
  }
}
