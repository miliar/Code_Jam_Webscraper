#include <cstdio>

int first[4][4];
int second[4][4];

int main()
{
  int ntest, count;

  scanf(" %d", &ntest);

  for( int cur_test = 1; cur_test <= ntest ; cur_test++ )
  {
    int fc, sc, card;

    count = 0;

    scanf(" %d", &fc);
    fc--;
    for(int i = 0; i < 4; i++)
      for (int j = 0; j < 4; ++j)
      {
        scanf(" %d", &( first[i][j] ) );
      }

    scanf(" %d", &sc);
    sc--;
    for(int i = 0; i < 4; i++)
      for (int j = 0; j < 4; ++j)
      {
        scanf(" %d", &( second[i][j] ) );
      }

    for (int i = 0; i < 4; ++i)
    {
      for( int j = 0; j < 4; ++j )
      {
        if(first[fc][i] == second[sc][j] )
        {
          count++;
          card = first[fc][i];
        }

      }
    }

    if( cur_test > 1 )
      printf("\n");

    printf("Case #%d: ", cur_test );
    if( count == 0 )
      printf("Volunteer cheated!");
    else if( count == 1 )
      printf("%d", card);
    else
      printf("Bad magician!");

  }

}