
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <map>
#include <vector>
#include <list>
#include <unordered_set>
#include <algorithm>

using namespace std;

#define ITER(_i, _o) for(typeof((_o)->begin()) _i = (_o)->begin(); _i != (_o)->end(); ++_i)
#define FIND(_i, _o, _key) typeof((_o)->begin()) _i = (_o)->find(_key)

FILE *ifile, *ofile;

long T;                          // num test cases

int read_input(const char *fbase="Sample")
{
  char fname[2048];

  // open input file with extension .in
  strncpy(fname, fbase, sizeof(fname) - 5);
  int fbase_idx = strlen(fname);
  strcpy(&fname[fbase_idx], ".in");
  ifile = fopen(fname, "r");
  assert(ifile);

  // open output file with extension .out
  strcpy(&fname[fbase_idx], ".out");
  ofile = fopen(fname, "w");
  assert(ofile);

  // scan the number of test cases
  fscanf(ifile, "%ld", &T);
  return 0;
} /* read_input */

int comp(const void *v1, const void *v2)
{
  long *l1 = (long *)v1;
  long *l2 = (long *)v2;
  return *l1 - * l2;
}

//  qsort(board, 512, sizeof(board[0]), comp);

unsigned long long U, L;
int read_test_case(long tc_id)
{
  fscanf(ifile, "%lld %lld", &L, &U);
} /* read_test_case */

unsigned long long cache [] = { 1,
                                4,
                                9,
                                121,
                                484,
                                10201,
                                12321,
                                14641,
                                40804,
                                44944,
                                1002001,
                                1234321,
                                4008004,
                                100020001,
                                102030201,
                                104060401,
                                121242121,
                                123454321,
                                125686521,
                                400080004,
                                404090404,
                                10000200001,
                                10221412201,
                                12102420121,
                                12345654321,
                                40000800004,
                                1000002000001,
                                1002003002001,
                                1004006004001,
                                1020304030201,
                                1022325232201,
                                1024348434201,
                                1210024200121,
                                1212225222121,
                                1214428244121,
                                1232346432321,
                                1234567654321,
                                4000008000004,
                                4004009004004,
                                100000020000001,
                                100220141022001,
                                102012040210201,
                                102234363432201,
};

char *solve(long tc_id)
{
  long strid = 0;
  static char result_str[65535];

  assert(!feof(ifile));
  tc_id++; // increment tc_id so that Case # will start from 1
  read_test_case(tc_id);

  strid += sprintf(&result_str[strid], "Case #%ld: ", tc_id);

  /* SOLVE HERE */
  unsigned long long *u = upper_bound(&cache[0], &cache[42], U);
  unsigned long long *l = lower_bound(&cache[0], &cache[42], L);
  long ans = u - l;

  strid += sprintf(&result_str[strid], "%ld\n", ans);

  return result_str;
} /* solve */

int main(int argc, char *argv[])
{
  char *str;
  read_input(argc > 1 ? argv[1] : "Sample");
  for (long i = 0; i < T; ++i) {
    str = solve(i);
    fprintf(ofile, "%s", str);
    fprintf(stderr, "%s", str);
  }
  return 0;
}
