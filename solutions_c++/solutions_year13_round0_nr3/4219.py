#include <cstdio>
#include <cstdlib>
using namespace std;
long long origin[] = {
1, 2, 3,
11, 22,
101, 111, 121, 202, 212,
1001, 1111, 2002,
10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102,
100001, 101101, 110011, 111111, 200002,
1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002};
long long v[40];

int main() {
  int t;
  FILE* fout = fopen("output.txt","w");
  FILE* fin = fopen("input.txt","r");
  fscanf(fin, "%d", &t);
  for(int k = 0; k < 40; k ++)
    v[k] = origin[k] * origin[k];
  for(int k = 1; k <= t; k ++) {
    long long l, r;
    int ans = 0;
    fscanf(fin, "%I64d%I64d", &l, &r);
    for(int i = 0; i < 40; i ++)
      if(v[i] <= r && v[i] >= l)
        ans ++;
    fprintf(fout, "Case #%d: %d\n", k, ans);
  }
  fclose(fin);
  fclose(fout);
  return 0;
}
