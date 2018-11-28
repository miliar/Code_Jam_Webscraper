#include <stdio.h>
#include <stdlib.h>
bool isspace(char a) { return a==' ' ? true : false;}
void solve_the_case(int case_num){
  int S_max, level;
  int need_friend = 0;
  int people_standing = 0;
  char special_case;
  char c;
  scanf("%d", &S_max);
  if (S_max == 0 ){
    printf("Case #%d: %d\n", case_num, 0);
    while ( (c=getchar()) != EOF && c != '\n' );
  } else{
    for (level=0; level<=S_max; level++){
      char stand_in_this_level;
      do{
            stand_in_this_level = getchar();
      }while (isspace(stand_in_this_level));
      int this_level = atoi(&stand_in_this_level);
      if (people_standing >= level || this_level==0){
        people_standing += this_level;
      }else{
        need_friend += level - people_standing;
        people_standing += this_level + level - people_standing;
      }
    }
    printf("Case #%d: %d\n", case_num, need_friend);
  }
  return;
}
int main(){
  int T, i;
  scanf("%d", &T);
  for (i = 1; i<=T; ++i )
    solve_the_case(i);

  return 0;
}
