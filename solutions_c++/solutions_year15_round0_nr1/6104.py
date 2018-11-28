#include <cstdio>
#include <cstring>

int main(){
  int minFriends;
  int T, smax, standingPeople;
  char sLevel[1002];
  scanf("%d", &T);

  for (int caseNum = 1; caseNum <= T; caseNum++){
    standingPeople = 0;
    minFriends = 0;
    scanf("%d %s", &smax, sLevel);

    for (int i = 0; i < strlen(sLevel); i++){
      int digit = (int)(sLevel[i] - '0');
      if (digit != 0){
        if (standingPeople < i){
          minFriends += i - standingPeople;
          standingPeople = i;
        }

        standingPeople += digit;
      }
    }

    printf("Case #%d: %d\n", caseNum, minFriends);
  }

	return 0;
}
