#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int main () {
  int T;
  scanf("%d", &T);
  for(int caso = 1; caso <= T; caso++) {
    int n;
    scanf("%d", &n);
    int v[2510] = {};
    for(int i = 0; i < 2*n-1; i++) {
      for(int j = 0; j < n; j++) {
        int x;
        scanf("%d", &x);
        v[x]++;
        //printf("%d\n", v[x]);
      }
    }
    vi resp;
    for(int i = 0; i <= 2500; i++)
       if(v[i]%2) resp.push_back(i);
    printf("Case #%d:",caso);
    for(int i = 0; i < resp.size(); i++) {
      printf(" %d", resp[i]);
    }
    printf("\n");
  }
  return 0;    
}
