#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;
string tab[100000][3]; // R P S
int main(){
  tab[1][0] = "R";
  tab[1][1] = "P";
  tab[1][2] = "S";
  for(int k = 2 ; k <= (1<<13) ; k*=2 ){
    string one,two;

    //R
    one = tab[k/2][0]+tab[k/2][2];
    two = tab[k/2][2]+tab[k/2][0];
    if( one < two ) tab[k][0] = one;
    else tab[k][0] = two;
    //P
    one = tab[k/2][1]+tab[k/2][0];
    two = tab[k/2][0]+tab[k/2][1];
    if( one < two ) tab[k][1] = one;
    else tab[k][1] = two;
    //S
    one = tab[k/2][1]+tab[k/2][2];
    two = tab[k/2][2]+tab[k/2][1];
    if( one < two ) tab[k][2] = one;
    else tab[k][2] = two;
  }
  int t;
  scanf("%d",&t);
  for(int e = 0 ; e <t ; e++ ){
    int n,g[3];
    scanf("%d",&n);
    for(int i = 0 ; i < 3 ; i++ ) scanf("%d",&g[i]);
    string ans = "Z";
    for(int i = 0 ; i < 3 ; i++ ){
      int c[3];
      c[0] = c[1] = c[2] = 0;
      for(int j = 0 ; j < tab[1<<n][i].length() ; j++ ){
        if( tab[1<<n][i][j] == 'R' ) c[0]++;
        if( tab[1<<n][i][j] == 'P' ) c[1]++;
        if( tab[1<<n][i][j] == 'S' ) c[2]++;
      }
      if( c[0] == g[0] && c[1] == g[1] && c[2] == g[2] ){
        if( tab[1<<n][i] < ans ) ans = tab[1<<n][i];
      }
    }
    printf("Case #%d: ",e+1);
    if( ans == "Z" ) printf("IMPOSSIBLE\n");
    else cout << ans << endl;
  }
}
      
