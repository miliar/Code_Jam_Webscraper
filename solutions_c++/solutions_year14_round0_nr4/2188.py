#include <cstdio>
#include <algorithm>
using namespace std;

int T;
int N;
double naomi[1005];
double ken[1005];
int ans1, ans2;

int main(){
  int i, j;

  freopen( "D-large.in", "r", stdin);
  freopen( "D-large.txt", "w", stdout);

  scanf("%d", &T);
  for( int tt = 1; tt <= T; tt++){
    scanf("%d", &N);
    for( i = 0; i < N; i++)
      scanf("%lf", &naomi[i]);
    for( i = 0; i < N; i++)
      scanf("%lf", &ken[i]);

    sort( naomi, naomi + N);
    sort( ken, ken + N);

    // for( i = 0; i < N; i++)
    //   printf("%lf ", naomi[i]);
    // printf("\n");
    // for( j = 0; j < N; j++)
    //   printf("%lf ", ken[j]);
    // printf("\n");


    i = j = N - 1;
    while( j >= 0){
      if( naomi[i] > ken[j])i--, j--;
      else j--;
    }
    ans1 = N - i - 1;

    i = j = 0;
    while( naomi[i] > ken[j] && j < N)j++;
    while( i < N && j < N){
      i++, j++;
      while( naomi[i] > ken[j] && j < N)j++;
    }
    ans2 = N - i;

    printf("Case #%d: %d %d\n", tt, ans1, ans2);
  }
}
