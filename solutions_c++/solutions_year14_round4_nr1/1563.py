#include <cstdio>
#include <algorithm>
using namespace std;

int T;
int ans;
int N;
int X;
int a[10005];

int main(){
  int i, j;

  freopen( "A-large.in", "r", stdin);
  freopen( "Data_Packing_l.txt", "w", stdout);

  scanf("%d", &T);
  for( int tt = 1; tt <= T; tt++){
    scanf("%d %d", &N, &X);
    for( i = 0; i < N; i++)
      scanf("%d", &a[i]);

    sort( a, a + N);
    
    ans = 0;
    i = 0, j = N - 1;
    while( i <= j){
      if( i == j){
	i++, ans++;
      }
      else{
	if( a[i] + a[j] > X)ans++, j--;
	else{
	  ans++;
	  i++, j--;
	}
      }
    }

    printf("Case #%d: %d\n", tt, ans);
  }
}
