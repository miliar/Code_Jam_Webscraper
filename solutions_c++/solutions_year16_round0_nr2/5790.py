#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxl = 100;
char str[maxl+5];

void flip(int j, bool reverse) {
  for(int i = 0; i <= j; i++) {
    str[i] = str[i] == '+' ? '-' : '+';
  }
  if(reverse) {
    for(int i = 0; i >= 0; i++) {
      int ii = j - i;
      if(i >= ii)
	break;
      swap(str[i], str[ii]);
    }
  }
}

int solve(int j) {
  if(j == -1) {
    return 0;
  } else {
    if(str[j] == '+') {
      int k;
      for(k = j - 1; k >= 0; k--) {
	if(str[k] == '-')
	  break;
      }
      return solve(k);
    } else {
      if(str[0] == '+') {
	flip(j, false);
	return solve(j) + 1;
      } else {
	flip(j, true);
	return solve(j) + 1;
      }
    }
  }
}

int main() {
  int tc;
  scanf("%d\n", &tc);
  for(int kase = 1; kase <= tc; kase++) {
    scanf("%s\n", str);
    int len = strlen(str);
    printf("Case #%d: %d\n", kase, solve(len - 1));
  }
  return 0;
}
