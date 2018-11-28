#include <bits/stdc++.h>
using namespace std;

int main(){
  int T,a,b,one[4][4],two[4][4],caso=0;
  scanf("%i",&T);
  while(T--){
    scanf("%i",&a);
    for(int i = 0; i<4; i++){
      for(int j = 0; j<4 ; j++) scanf("%i",&one[i][j]);
    }
    scanf("%i",&b);
    for(int i = 0; i<4; i++){
      for(int j = 0; j<4 ; j++) scanf("%i",&two[i][j]);
    }
    a--;
    b--;
    int cont = 0,num;
    for(int i = 0; i<4;i++){
      for(int j = 0; j<4; j++) {
        if(one[a][i] == two[b][j]) {
          num = one[a][i];
          cont++;
        }
      }
    }
    printf("Case #%i: ", ++caso);
    if(cont == 0) puts("Volunteer cheated!");
    if(cont == 1) printf("%i\n", num);
    if(cont > 1) puts("Bad magician!");
  }
  return 0;
}