// Problem B. Lawnmower
// Contest: Google CodeJam Qualification Round 2013
// Author: LotK

#include <cstdio>

int main() {
  int t, tt, n, m, i, j, max;
  int a[105][105], tmp[105][105];
  int horizontal[105], vertical[105];
  scanf("%d", &tt);
  for(t=0 ; t<tt; t++) {
    scanf("%d%d", &n, &m);
    for(i=0 ; i<n ; i++) {
      for(j=0 ; j<m ; j++) {
        tmp[i][j]=100;
      }
    }

    for(i=0 ; i<n ; i++) {
      max=0;
      for(j=0 ; j<m ; j++) {
        scanf("%d", &a[i][j]);
        if(max<a[i][j]) max = a[i][j];
      }
      horizontal[i]=max;
    }
    for(i=0 ; i<m ; i++) {
      max=0;
      for(j=0 ; j<n ; j++) {
        if(max<a[j][i]) max = a[j][i];
      }
      vertical[i]=max;
    }

    for(i=0 ; i<n ; i++) {
      for(j=0 ; j<m ; j++) {
        if(tmp[i][j]>horizontal[i]) tmp[i][j]=horizontal[i];
      }
    }
    for(i=0 ; i<m ; i++) {
      for(j=0 ; j<n ; j++) {
        if(tmp[j][i]>vertical[i]) tmp[j][i]=vertical[i];
      }
    }

    /*
    printf("\n");
    for(i=0 ; i<n ; i++) {
      for(j=0 ; j<m ; j++) {
        printf("%d ", tmp[i][j]);
      }
      printf("\n");
    }
    printf("\n");
    */
    for(i=0 ; i<n ; i++) {
      for(j=0 ; j<m ; j++) {
        if(a[i][j] != tmp[i][j]) break;
      }
      if(j<m) break;
    }
    printf("Case #%d: ", t+1);
    if(i==n) printf("YES\n");
    else printf("NO\n");
  }
}
