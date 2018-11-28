#include <cstdio>

using namespace std;

int main()
{
  int tc, ti;
  scanf("%d",&tc);
  for (ti =1 ; ti <= tc; ++ti) {
    int n,r,c;
	scanf("%d %d %d", &n, &r, &c);
	if ((r*c) % n != 0) {
	  printf("Case #%d: RICHARD\n", ti);
	  continue;
	}
	int t;
	if ( r > c) {
	  t = r;
	  r = c;
	  c = t;
	}
	switch (n) {
	case 1:
	  printf("Case #%d: GABRIEL\n", ti);  
	  continue;
	
	case 2:
	  printf("Case #%d: GABRIEL\n", ti);
	  continue;
	
	case 3:
	  if ( r == 1)
        printf("Case #%d: RICHARD\n", ti);
	  else
	    printf("Case #%d: GABRIEL\n", ti);
	  continue;
	  
	case 4:
	  if ( r == 1 || r == 2)
        printf("Case #%d: RICHARD\n", ti);	
	  else
	    printf("Case #%d: GABRIEL\n", ti);
      continue;
    }
  }
  return 0;
}