#include<stdio.h>
#include<string.h>

int N = 0;
char numbers[50000][200];
char A[200], B[200];

int cmp(char *A, char *B) {
  if(strlen(A) != strlen(B)) return strlen(A) - strlen(B);
  return strcmp(A,B);
}

void go(int t) {
  scanf("%s %s",A,B);
  int i,cnt=0;
  for(i=0;i<N;i++) {
    if(cmp(numbers[i],A)<0) continue;
    if(cmp(numbers[i],B)>0) continue;
    cnt++;
  }
  printf("Case #%d: %d\n",t,cnt);
}

int main() {
  int t,T=1;

  FILE *fin = fopen("palindromes.txt","r");
  while(fscanf(fin,"%s",numbers[N]) == 1) N++;
  fclose(fin);
  
  scanf("%d",&T);
  for(t=1;t<=T;t++) go(t);
  return 0;
}
