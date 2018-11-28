#include <stdio.h>
#include <math.h>
#include <string.h>
#include <malloc.h>

bool pal(long long int i) {

  char line[1000];  
  
  sprintf(line,"%lld",i);

  int len = strlen(line);

  for (int p = 0; p <= len/2; p++) {
    if (line[p] != line[len-p-1]) {
      return false;
    }
  }
  return true;
}

bool fs(long long int i) {

  long long int r = i*i;
      
  return (pal(i) && pal(r)); 
}

main() {

  int T;

  long long int *fst;
  fst = (long long int *) malloc(10000002 * sizeof(long long int));
  fst[0] = 1;

  for (long long int sa = 1; sa <= 10000000; sa++) {
    if (fs(sa)) {
      fst[sa] = fst[sa-1]+1;
    }
    else 
      fst[sa] = fst[sa-1];
  }
       
    

  scanf("%d",&T);

  for (int t = 1; t <= T; t++) {
    long long int a,b;

    scanf("%lld %lld",&a,&b);

    long long int sa = (long long int) sqrt(a);
    if (sa*sa < a) 
      sa++;
    long long int sb = (long long int) sqrt(b);
    
    long long np = fst[sb] - fst[sa-1];

    printf("Case #%d: %lld\n",t,np);
  }


}
