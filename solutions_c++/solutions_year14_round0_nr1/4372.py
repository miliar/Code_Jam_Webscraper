#include <stdio.h>

class Trick{
  public:
  int firstSet[4][4];
  int secondSet[4][4];
  int firstAnswer, secondAnswer;
  
  
  
  void fill(){
    scanf("%d", &firstAnswer);
    for (int i = 0; i < 4; i++){
      for (int j = 0; j < 4; j++){
        scanf("%d", &firstSet[i][j]);
      }
    }
    scanf("%d", &secondAnswer);
    for (int i = 0; i < 4; i++){
      for (int j = 0; j < 4; j++){
        scanf("%d", &secondSet[i][j]);
      }
    }
  }
  
  void solve(){
    int n = 0;
    int a;
    for (int i = 0; i < 4; i++){
      for (int j = 0; j < 4; j++){
        if (firstSet[firstAnswer-1][i] == secondSet[secondAnswer-1][j]){
          a = firstSet[firstAnswer-1][i];
          n++;
        }
      }
    }
    
    if (n == 0){
      printf("Volunteer cheated!\n");
    } else if (n == 1){
      printf("%d\n",a);
    } else {
      printf("Bad magician!\n");
    }
    
  }
  
  
};

int main()
{
   
   int n;
   scanf("%d", &n);
   Trick t;
   for(int i =1; i <= n; i++){
    t.fill();
    printf("Case #%d: ",i);
    t.solve();  
   };

   return 0;
}
