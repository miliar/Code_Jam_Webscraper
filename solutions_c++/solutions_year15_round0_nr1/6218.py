#include <cstdio>
#include <algorithm>

using namespace std;


int intofchar(char c){
   return (int)c -(int)'0';
}
int main(){
   int nbTests;
   scanf("%d", &nbTests);
   for(int i=0; i<nbTests; i++){
      int valMax;
      scanf("%d", &valMax);
      int mini = 0;
      int tot = 0;
      for(int j=0; j<=valMax; j++){
         char c;
         scanf(" %c", &c);
         int val = intofchar(c);
         mini = max(mini, j-tot);
         tot+=val;
      }
      printf("Case #%d: %d\n", (i+1), mini);
   }

}