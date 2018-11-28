#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

FILE *in = fopen("C.in", "r");
FILE *out = fopen("C.out", "w");

long long a[1111111], na;
char str[111];
bool good(long long x){
  int nstr = 0;
  while(x){
    str[nstr ++] = x % 10;
    x /= 10;
  }
  for(int q = 0; q < nstr - q - 1; q++){
    if(str[q] != str[nstr - q - 1]) return 0;
  }
  return 1;
}

int search(long long val){
  int s = 0, e = na - 1, ans = -1;
  while(s <= e){
    int mid = (s + e) >> 1;
    if(a[mid] <= val){
      ans = mid;
      s = mid + 1;
    }
    else{
      e = mid - 1;
    }
  }
  return ans;
}

int main(){
  
  na = 0;
  for(long long x = 1; x * x <= 100000000000000ll; x++){
    if(good(x) && good(x * x)){
      a[na ++] = x * x;
    }
  }
  int ntest;
  fscanf(in, "%d", &ntest);
  for(int test = 1; test <= ntest; test++){
    long long A, B;
    fscanf(in, "%lld%lld", &A, &B);
    int rA = search(A - 1), rB = search(B);
    int ans = rB - rA;
    if(rB == -1 || a[rB] < A) ans = 0;
    fprintf(out, "Case #%d: %d\n", test, ans);
  }
  
  return 0;
}
