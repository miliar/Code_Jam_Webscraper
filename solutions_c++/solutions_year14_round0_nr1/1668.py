#include <stdio.h>

int main(){

int T =0;

scanf("%d", &T);


for(int k = 1; k<=T; k++){
  int n1=0;
  scanf("%d", &n1);
  n1--;
  //printf("%d\n", n1);
  int array[4][4];
  for(int i=0; i<4; i++)
    for(int j = 0; j<4; j++)
      scanf("%d", &array[i][j]);
  int n2=0;
  scanf("%d", &n2);
  n2--;
  int newarray[4][4];
  for(int i=0; i<4; i++)
    for(int j = 0; j<4; j++)
      scanf("%d", &newarray[i][j]);
  //printf("%d %d\n", n1, n2);
  int sol = -1;
  int n = 0;
  for(int i = 0; i<4; i++)
    for(int j = 0; j<4; j++){
      //printf("%d %d\n", array[n1][i] , newarray[n2][j]); 
      if(array[n1][i] == newarray[n2][j]){
	sol = array[n1][i];
	n ++;
      }
    }
  
  if(n == 0)
    printf("Case #%d: Volunteer cheated!\n", k);
  else if(n>1)
    printf( "Case #%d: Bad magician!\n", k);
  else
    printf( "Case #%d: %d\n", k, sol);
 
}

return 0;
}
