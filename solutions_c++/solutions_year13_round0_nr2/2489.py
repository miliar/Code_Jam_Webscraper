
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <algorithm>

using namespace std;

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

int N, M;
int lawn[100][100];
int read_test_case(long tc_id)
{
  fscanf(ifile, "%d %d\n", &N, &M);
  for (long i = 0; i < N; ++i) {
    for (long j = 0; j < M; ++j) {
      fscanf(ifile, "%d", &lawn[i][j]);
    } /* 'j' for loop */
  } /* 'i' for loop */

  return 0;
} /* read_test_case */

char *solve(long tc_id)
{
  long strid = 0;
  static char result_str[65535];

  assert(!feof(ifile));
  tc_id++; // increment tc_id so that Case # will start from 1
  read_test_case(tc_id);

  strid += sprintf(&result_str[strid], "Case #%ld: ", tc_id);

  /* SOLVE HERE */
  int h[100] = {0};
  int v[100] = {0};
  for (long i = 0; i < N; ++i) {
    int mx = 0;
    for (long j = 0; j < M; ++j) {
      mx = max(mx, lawn[i][j]);
    } /* 'j' for loop */
    h[i] = mx;
  } /* 'i' for loop */

  for (long j = 0; j < M; ++j) {
    int mx = 0;
    for (long i = 0; i < N; ++i) {
      mx = max(mx, lawn[i][j]);
    } /* 'j' for loop */
    v[j] = mx;
  } /* 'i' for loop */

  bool possible = true;
  for (long i = 0; i < N; ++i) {
    for (long j = 0; j < M; ++j) {
      int exp = min(h[i], v[j]);
      if (exp != lawn[i][j]) {
        possible = false;
        break;
      }
    } /* 'j' for loop */
  } /* 'i' for loop */


  strid += sprintf(&result_str[strid], "%s\n", possible ? "YES" : "NO");

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
