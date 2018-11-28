#include <stdio.h>

int table[8][8] = {
  {0, 1, 2, 3, 4, 5, 6, 7},
  {1, 0, 3, 2, 5, 4, 7, 6},
  {2, 3, 1, 0, 6, 7, 5, 4},
  {3, 2, 0, 1, 7, 6, 4, 5},
  {4, 5, 7, 6, 1, 0, 2, 3},
  {5, 4, 6, 7, 0, 1, 3, 2},
  {6, 7, 4, 5, 3, 2, 1, 0},
  {7, 6, 5, 4, 2, 3, 0, 1}
};

int main(int argc, char const *argv[])
{
  int t = 0;
  scanf("%d\n", &t);
  int conv[256];
  conv['i'] = 2;
  conv['j'] = 4;
  conv['k'] = 6;
  for (int ii = 0; ii < t; ii++) {
    int l, x;
    scanf("%d %d\n", &l, &x);
    int arr[10001];
    for (int i = 0; i < l; i++) {
      char temp;
      scanf("%c", &temp);
      arr[i] = conv[temp];
    }
    int arr_lx[10001];
    int lx = l*x;
    for (int i = 0; i < lx; i++) {
      arr_lx[i] = arr[i%l];
    }
    // compute value of arr_lx
    int val = 0;
    for (int i = 0; i < lx; i++) {
      val = table[val][arr_lx[i]];
    }
    if (val != 1) { // 1 is code for -1
      printf("Case #%d: NO\n", ii+1);
    } else {
      // find smallest i
      int i_index = lx+1;
      val = 0;
      for (int i = 0; i < lx; i++) {
        val = table[val][arr_lx[i]];
        if (val == 2) { // 2 is code for i
          i_index = i;
          break;
        }
      }
      // find largest k
      val = 0;
      int k_index = -1;
      for (int i = lx-1; i >= 0; i--) {
        val = table[arr_lx[i]][val];
        if (val == 6) { // 6 is code for k
          k_index = i;
          break;
        }
      }
      if (i_index < k_index) {
        printf("Case #%d: YES\n", ii+1);
      } else {
        printf("Case #%d: NO\n", ii+1);
      }
    }
  }
  return 0;
}