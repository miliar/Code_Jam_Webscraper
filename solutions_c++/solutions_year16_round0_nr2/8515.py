#include "cstdio"
void proc(int n){
  char v[111];
  char s[111];
  scanf("%s",v);
  int i=1;
  int cur = 1;
  s[0]=v[0];
  while (v[i]) {
    if(v[i]!=v[i-1])s[cur++]=v[i];
    i++;
  }
  printf("Case #%d: %d\n",n,s[cur-1]=='+'?cur-1:cur);
}
int main(int argc, char const *argv[]) {
  int q;
  scanf("%d\n", &q);
  for (size_t i = 0; i < q; i++) {
    proc(i+1);
  }
  return 0;
}
