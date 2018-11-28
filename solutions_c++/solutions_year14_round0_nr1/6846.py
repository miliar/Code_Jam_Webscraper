#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int main(int argc, char *argv[]) {

  int T, row, cardid;
  int cards[16];

  scanf("%d", &T);

  for(int t=1; t<=T; t++) {

    //First answer
    scanf("%d", &row);
    row--; //Index from [1-4] to [0-3]

    memset(cards, 0, 16*sizeof(int));

    //Read cards first arrangement
    for(int i=0; i<4; i++)
      for(int j=0; j<4; j++) {
	scanf("%d", &cardid);
	if( i == row )
	  cards[cardid-1]++;
      }

    //second answer
    scanf("%d", &row);
    row--; //Index from [1-4] to [0-3]

    //Read cards second arrangement
    for(int i=0; i<4; i++)
      for(int j=0; j<4; j++) {
	scanf("%d", &cardid);
	if( i == row )
	  cards[cardid-1]++;
      }

    //Compute solution
    int chosen = -1;

    // printf("info:");
    // for(int i=0; i<16; i++)
    //   if( cards[i]>0 )
    // 	printf(" (%d,%d)", i+1, cards[i]);
    // printf("\n");

    for(int i=0; i<16; i++)
      if( cards[i] == 2 ) {
	if( chosen < 0 ) chosen = i+1;
	else if( chosen > 0 ) chosen = 0;
      }
    
    //Print solution
    if( chosen > 0 )
      printf("Case #%d: %d\n", t, chosen);
    else if( chosen == 0 )
      printf("Case #%d: Bad magician!\n", t);
    else
      printf("Case #%d: Volunteer cheated!\n", t);
  }

  return 0;
}
