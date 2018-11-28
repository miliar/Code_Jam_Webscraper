#include <stdio.h>
#include <math.h>
#include <stdlib.h>

long n,j;
long a[33];
long b[20];
FILE *out;

bool isPrime(long k, long base) {
  if (k<=1)
    return false;
  else if (k<=3)
    return true;
  else if (k%2 == 0) {
    b[base] = 2;
    return false;
  }
  else if (k%3 == 0) {
    b[base] = 3;
    return false;
  }

  long i=5;
  while (i*i <= k) {
    if (k % i == 0) {
      b[base] = i;
      return false;
    }
    else if (k % (i+2) == 0) {
      b[base] = i+2;
      return false;
    }
    i = i + 6;
  }
  return true;
}

void check(long cur) {
  if (cur == n-1) {
    long k; long sum;
    for (long i=2; i<=10; i++) {
      k=1; sum=0;
      for (long l=0; l<n; l++) {
        sum += a[l]*k;
        k=k*i;
      }
      if (isPrime(sum,i)) {
        return;
      }
    }
    j = j-1;
    for (long l=n-1; l>=0; l--) {
      fprintf(out,"%ld",a[l]);
    }
    for (long l=2; l<=10; l++) {
      fprintf(out," %ld",b[l]);
    }
    fprintf(out,"\n");
    if (j == 0) {
      exit(0);
    }
  }
  else {
    a[cur] = 0;
    check(cur+1);
    a[cur] = 1;
    check(cur+1);
  }
}

int main(void){

  out = fopen("output.txt","w");
  // small data set
  n = 16; j = 50;
  // large data set
  //n = 32; j = 500
  for (long i=0; i<33; i++)
    a[i] = 0;

  a[0] = 1;
  a[n-1] = 1;

  fprintf(out,"Case #1:\n");
  check(1);

  return 0;
}
