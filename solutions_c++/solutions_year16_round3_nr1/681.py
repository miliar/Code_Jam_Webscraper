#include <bits/stdc++.h>
using namespace std;
#define forn(i, n) for(int i = 0; i < (int) (n); i++)
const int N = 50;

int n, A[N], s, TC, tc;

int main(){
  freopen("in.in", "r", stdin);
  freopen("out.out", "w", stdout);
  scanf("%d", &tc);
  while(tc--){
    scanf("%d", &n);
    forn(i, n){
      scanf("%d", &A[i]);
      s += A[i];
    }
    printf("Case #%d:", ++TC);
    while(s){
      printf(" ");
      int mx = -1, id = -1, sub = -1;
      forn(i, n){
        if(A[i] > mx){
          mx = A[i];
          id = i;
          sub = i;
        }
        else if(A[i] == mx){
          sub = i;
        }
      }
      if(A[id] > s / 2){
        printf("ESTO LA CAGA!\n");
        return 0;
      }
      if(A[id]){
        A[id]--;
        s--;
        printf("%c", id + 'A');
      }
      if(A[sub] && s != 2){
        A[sub]--;
        s--;
        printf("%c", sub + 'A');
      }
    }
    puts("");
  }
  return 0;
}
