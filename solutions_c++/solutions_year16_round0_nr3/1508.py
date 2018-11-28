#include<cstdio>
#include<vector>
#define MAX 1000
using namespace std;
int foundNum = 0;
bool prime[MAX+5];
int dig[50];
int T, N, J;
void generateNumber(int dig[], int pos, vector<int>& primes)
{
  int arr[9] = {2, 3, 4, 5, 6, 7, 8, 9, 10};
  int ans[9];
  int idx, i, j, k;
  if (foundNum >= J) {
    return;
  }
  if (pos == 0) {
    for (idx = 0; idx < 9; idx++) {
      for (i=0; i<primes.size(); i++) {
	j = 1;
	for (k=1; k<N; k++) {
	  j = (j*arr[idx]+dig[k])%primes[i];
	}
	if (j == 0)
	  break;
      }
      if (i>=primes.size()) {
	break;
      }
      ans[idx] = primes[i];
    }
    if (idx>=9) {
      for (i=0;i<N;i++) printf("%d",dig[i]);
      printf(" ");
      for (i=0;i<9;i++) {
	printf("%d ",ans[i]);
      }
      printf("\n");
      foundNum++;
    }
    return;
  }
  dig[pos] = 1;
  generateNumber(dig, pos-1, primes);
  dig[pos] = 0;
  generateNumber(dig, pos-1, primes);
}
int main()
{
  int i, j;
  vector<int> primes;
  for (i=2; i< MAX; i++) {
    prime[i] = true;
  }
  for (i=3; i+i+i<MAX; i++) {
    for(j=i+i+i; j<MAX; j+=(i+i)) {
      prime[j] = false;
    }
  }
  for(i=3; i<MAX; i+=2) {
    if (prime[i]) primes.push_back(i);
  }
  scanf("%d %d %d", &T, &N, &J);
  dig[0] = dig[N-1] = 1;
  printf("Case #1:\n");
  generateNumber(dig, N-2, primes);
  return 0;
}
