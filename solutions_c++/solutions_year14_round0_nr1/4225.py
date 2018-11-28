#include<cstdio>

int T;
int cards,card;
int a[2];
int arr[2][4][4];

int main(){
  scanf("%d",&T);
  for(int t=1;t<=T;t++){
    for(int k=0;k<2;k++){
      scanf("%d",&a[k]);
      a[k]--;
      for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
          scanf("%d",&arr[k][i][j]);
        }
      }
    }
    cards = 0;
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
        if(arr[0][a[0]][i] == arr[1][a[1]][j]){
          cards++;
          card = arr[0][a[0]][i];
        }
      }
    }
    printf("Case #%d: ",t);
    if(cards == 1) printf("%d\n",card);
    if(cards == 0) printf("Volunteer cheated!\n");
    if(cards > 1) printf("Bad magician!\n");
  }

  return 0;
}
