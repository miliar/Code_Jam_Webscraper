#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
  int T, n[17];
  
  scanf("%d", &T);
  for(int i=0; i<T; i++) {
    int l1, l2;
    memset(n,0,17*sizeof(int));
    scanf("%d", &l1);
    for(int j=0; j<16; j++) {
      int k;
      scanf("%d", &k);
      if(j/4==l1-1)
	n[k]=1;
    }

    scanf("%d", &l2);
    int vcheat = 1, bmag = 0, ans = 0;
    for(int j=0; j<16; j++) {
      int k;
      scanf("%d", &k);
      if(j/4==l2-1)
	if(n[k])
	  if(vcheat) {
	    vcheat = 0;
	    ans = k;
	  }
	  else
	    bmag = 1;
    }
    if(vcheat)
      printf("Case #%d: Volunteer cheated!\n", i+1);
    else
      if(bmag)
	printf("Case #%d: Bad magician!\n", i+1);
      else
	printf("Case #%d: %d\n", i+1, ans);
  }
    
  return 0;
}
