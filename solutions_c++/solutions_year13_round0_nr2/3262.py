#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

using namespace std;

static const char *sentence[] = {
  "YES",
  "NO"
};

static int process(const int *tab, int *tab_lin, int *tab_col, int nb_line,
  int nb_col)
{
  for (int i = 0; i < nb_col * nb_line; i++) {
    int l = i/nb_col;
    int c = i - (i/nb_col) * nb_col;
    int max;

    /* Compute max on lth line */
    if (tab_lin[l] == -1) {
      max = tab[i];
      for (int j = 0; j < nb_col; j++)
        if (tab[nb_col * l + j] > max)
          max = tab[nb_col * l + j];
      tab_lin[l] = max;
    }

    /* Compute max on cth column*/
    if (tab_col[c] == -1) {
      max = tab[i];
      for (int j = 0; j < nb_line; j++)
        if (tab[nb_col * j + c] > max)
          max = tab[nb_col * j + c];
      tab_col[c] = max;
    }

    /* Check Lawnmower path possibility */
    if ((tab[i] < tab_lin[l]) && ((tab[i] < tab_col[c])))
      return 1;
  }

  // for (int i = 0; i < nb_col * nb_line; i++)
  //   printf("%d ", tab[i]);

  // printf("\n");

  // for (int i = 0; i < nb_col; i++)
  //   printf("%d ", tab_col[i]);

  // printf("\n");

  // for (int i = 0; i < nb_line; i++)
  //   printf("%d ", tab_lin[i]);


  return 0;
}




int main(int argc, const char *argv[])
{
  if (argc != 2)
    return 1;
  const char *filename = argv[1];

  FILE *f = fopen(filename, "r");
  if (f == NULL)
    return 2;

  int nb_test;
  fscanf(f, "%d", &nb_test);

  char a;
  fscanf(f, "%c", &a);

  for (int i = 0; i < nb_test; i++) {
    int nb_line;
    int nb_col;
    fscanf(f, "%d", &nb_line);
    fscanf(f, "%d", &nb_col);
    fscanf(f, "%c", &a);

    int *tab_max_line = (int *)malloc(nb_line * sizeof(int));
    int *tab_max_col = (int *)malloc(nb_col * sizeof(int));
    int *tab = (int *)malloc(nb_line * nb_col * sizeof(int));

    for (int j = 0; j < nb_line; j++) {
      for (int k = 0; k < nb_col; k++) {
        fscanf(f, "%d", &tab[nb_col * j + k]);
      }
      fscanf(f, "%c", &a);
    }

    for (int j = 0; j < nb_line; j++)
      tab_max_line[j] = -1;

    for (int j = 0; j < nb_col; j++)
      tab_max_col[j] = -1;

    printf("Case #%d: %s\n", i + 1,
      sentence[process(tab, tab_max_line, tab_max_col, nb_line, nb_col)]);

    free(tab_max_line);
    free(tab_max_col);
    free(tab);
  }


  return 0;
}
