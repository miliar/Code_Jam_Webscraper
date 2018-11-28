#include<cstdio>

int a[4][4], b[4][4];

void readMatrix(int c[][4]) {
    for(int i = 0;  i < 4; i++) {
      for(int j = 0; j < 4; j++ )
	scanf("%d", &c[i][j]);
    }
}

void solve(int l1, int l2) {
  int k = 0;
  int auxiliary;
  for(int i = 0; i < 4; i++) {
    for(int j = 0;  j < 4; j++) {
      if(a[l1][i] == b[l2][j]) {
	auxiliary = a[l1][i];
	k++;
      }
    }
  }
  if(k > 1) printf("Bad magician!\n");
  else if(k == 0) printf("Volunteer cheated!\n");
  else printf("%d\n", auxiliary);
}


int main() {
  freopen("A-small-attempt0.in", "r", stdin);
  freopen("o.out","w", stdout);

  int n; scanf("%d",&n);
  int line1, line2;
  int counter;

  for(counter = 1; counter <= n; counter++){
    scanf("%d", &line1);
    readMatrix(a);
    scanf("%d", &line2);
    readMatrix(b);
    printf("Case #%d: ",counter);
    solve(line1 - 1,line2 - 1);  
  }
  return 0;
}
