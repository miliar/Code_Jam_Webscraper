#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <iostream>

static void read_grid(int32_t grid[4][4])
{
    for (int32_t i = 0; i < 4; ++i) {
        for (int32_t j = 0; j < 4; ++j) {
            std :: cin >> grid[i][j];
        }
    }
#ifdef DEBUG
    for (int32_t i = 0; i < 4; ++i) {
        for (int32_t j = 0; j < 4; ++j) {
            fprintf(stdout, "%d ", grid[i][j]);
        }
        fprintf(stdout, "\n");
    }
#endif // DEBUG
}

static int32_t do_magic(void)
{
  int32_t grid[4][4];
  int32_t row;
  int32_t ret = 0;
  bool possible_cards[17];

    memset(possible_cards, 0, 17*sizeof(bool));

    std :: cin >> row;
    row--;
    read_grid(grid);

    for (int32_t i = 0; i < 4; ++i) {
        possible_cards[grid[row][i]] = true;
    }

    std ::cin >> row;
    row--;
    read_grid(grid);


    for (int32_t i = 0; i < 4; ++i) {
        if (possible_cards[grid[row][i]]) {
            if (ret == 0) {
                ret = grid[row][i];
            }
            else {
              return -1;
            }
        }
    }
  return ret;
}

int32_t main(int32_t argc, char **argv)
{
  int32_t T;

  std :: cin >> T;

    for (int32_t i = 1; i <= T; ++i) {
      int32_t card = do_magic();

        fprintf(stdout, "Case #%d: ", i);

        switch (card) {
            case -1:
                fprintf(stdout, "Bad magician!\n");
              break;
            case 0:
                fprintf(stdout, "Volunteer cheated!\n", i);
              break;
            default:
                fprintf(stdout, "%d\n", card);
              break;
        }
    }
  return 0;
}
