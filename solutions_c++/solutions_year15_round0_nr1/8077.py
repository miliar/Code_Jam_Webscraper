#include <iostream>
#include <stdio.h>
using namespace std;
inline void frs(char *str) {
  register char c = 0;
  register int i = 0;
  while (c < 33)
      c = getchar_unlocked();
  while (c != '\n') {
      str[i] = c;
      c = getchar_unlocked();
      i = i + 1;
  }
  str[i] = '\0';
}
inline void fri(int *x) 
{
  register int c = getchar_unlocked();
  *x = 0;
  int neg = 0;
  for(; ((c<48 || c>57) && c != '-'); 
  c = getchar_unlocked());
  if(c=='-') {
      neg = 1;
      c = getchar_unlocked();
  }
  for(; c>47 && c<58 ; c = getchar_unlocked()) {
      *x = ((*x)<<1) + ((*x)<<3) + c - 48;
  }
  if(neg)
      *x = -(*x);
}
int main() {
	int t, s, i, sp, rp, ans, k;
	char levels[1002];
	fri(&t);
	for(k = 1;k <= t;k++) {
		fri(&s);
		frs(levels);
		sp = levels[0] - '0';
		rp = 1;
		ans = 0;
		for(i = 1;i <= s;i++, rp++) {
			if(rp > sp) {
				ans += (rp - sp);
				sp = rp;
			}
			sp += levels[i] - '0';
		}
		cout << "Case #" << k << ": " << ans << "\n";
	}
	return 0;
}