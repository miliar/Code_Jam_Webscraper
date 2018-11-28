#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <math.h>

using namespace std;

/* return true if val is a palindrom. */
static bool is_pal(int val)
{
  char tab[100];
  int sz = 0;

  while (val != 0) {
    tab[sz] = val - (val / 10) * 10;
    sz++;
    val /= 10;
  }

  for (int i = 0; i < sz; i++)
    if (tab[i] != tab[sz - i - 1])
      return false;

  return true;
}


static int int_sqrt(int val)
{
  double double_sqrt = sqrt(val);
  int int_sqrt = (int) double_sqrt;
  if ((double_sqrt - (double)int_sqrt) != 0)
    return 0;
  return int_sqrt;
}

static int process(int lower, int upper)
{
  int cnt = 0;
  for (int i = lower; i <= upper; i++ ) {

    if (!is_pal(i))
      continue;

    int sq = int_sqrt(i);
    if (sq == 0)
      continue;

    if (!is_pal(sq))
      continue;

    cnt++;
  }

  return cnt;
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
    int lower;
    int upper;
    fscanf(f, "%d", &lower);
    fscanf(f, "%d", &upper);
    fscanf(f, "%c", &a);


    printf("Case #%d: %d\n", i + 1, process(lower, upper));
  }

  // for (int i = 0; i < 1000; i++)
  //   printf("%s: %5d %5d\n", is_pal(i)? "PAL": "---", i, int_sqrt(i));

  return 0;
}
