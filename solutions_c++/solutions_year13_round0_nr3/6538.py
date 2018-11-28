#include <cstdio>
#include <cstring>

bool palindrome(int num) {
  char cad[10];
  int pos=0;
  while(num) {
    cad[pos++] = num%10;
    num /= 10;
  }
  for(int i=0; i<pos/2; i++){
    if(cad[i] != cad[pos - i -1]) return 0;
  }
  return 1;
}

int main(){ 
  
  int g[1005];
  
  memset(g, 0, sizeof(g));
  
  for(int i=1; i*i<1005; i++) 
    if( palindrome(i) && palindrome(i*i) ){
      //printf("num : %d\n", i*i);
      g[i*i+1] = 1;
    }
  //printf("\n");
  for(int i = 2; i<1005; i++){
    g[i] += g[i-1];
    //printf("g[%d] : %d\n", i, g[i]);
  }
  //printf("\n");

  int n_test, a, b;
  scanf("%d", &n_test);
  for(int i=1; i<=n_test; i++){
    scanf("%d%d", &a, &b);
    printf("Case #%d: %d\n", i, (g[b+1] - g[a]));
  }
return 0;}
