#include <cstdio>

int main(){
  int T;
  scanf("%d",&T);
  for(int t=1; t<=T; ++t){
    int firstRow;
    scanf("%d",&firstRow);
    firstRow--;
    int firstDeck[4][4];
    for(int i=0; i<4; ++i){
      for(int j=0; j<4; ++j){
        scanf("%d",&(firstDeck[i][j]));
      }
    }
    int secondRow;
    scanf("%d",&secondRow);
    secondRow--;
    int secondDeck[4][4];
    for(int i=0; i<4; ++i){
      for(int j=0; j<4; ++j){
        scanf("%d",&(secondDeck[i][j]));
      }
    }
    int numOfPossibleCards = 0;
    int card = 0;
    for(int i=0; i<4; ++i){
      for(int j=0; j<4; ++j){
        if(firstDeck[firstRow][i] == secondDeck[secondRow][j]){
          numOfPossibleCards++;
          card = firstDeck[firstRow][i];
        }
      }
    }
    printf("Case #%d: ",t);
    if(numOfPossibleCards == 0){
      printf("Volunteer cheated!\n");
    }else if(numOfPossibleCards == 1){
      printf("%d\n",card);
    }else{
      printf("Bad magician!\n");
    }
  }
}
