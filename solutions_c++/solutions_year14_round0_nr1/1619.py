
#include <stdio.h>

#include <map>

using namespace std;

main() {

  
  int T;
  
  scanf("%d",&T);
  
  for (int t = 1; t <= T; t++) {
    
    int r;
    int s;
    scanf("%d",&r);
    map <int , int> values;
    for (int l = 1; l <= 4; l++)
      {
	int a;
	for (int j = 1; j <= 4; j++) {
	  scanf("%d",&a);
	  if (l == r) {
	    values[a] = 1;
	  }
	}
      }

    scanf("%d",&s);
    int match = 0;
    int matches = 0;
    for (int l = 1; l <= 4; l++)
      {
	int a;
	for (int j = 1; j <= 4; j++) {
	  scanf("%d",&a);
	  if (l == s) {
	    if (values[a] == 1) {
	      matches++;
	      match = a;
	    }
	  }
	}
      }
    
    if (matches == 1) {
      printf("Case #%d: %d\n",t,match);
    }
    if (matches > 1) {
      printf("Case #%d: Bad magician!\n",t);
    }
    if (matches == 0) {
      printf("Case #%d: Volunteer cheated!\n",t);
    }
    
  }

}
