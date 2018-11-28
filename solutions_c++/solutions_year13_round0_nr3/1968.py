#include <stdio.h>
#include <string.h>
#include <math.h>

int tree[10000100];
int MaxVal = 10000010;

int read(int idx){
	int sum = 0;
	while (idx > 0){
		sum += tree[idx];
		idx -= (idx & -idx);
	}
	return sum;
}

void update(int idx ,int val){
	while (idx <= MaxVal){
		tree[idx] += val;
		idx += (idx & -idx);
	}
}

char tmp[50];
bool testpal(long long int n) {
  sprintf(tmp, "%lld", n);
  int s = strlen(tmp);
  for (int i = 0; i < s/2; i++) {
    if (tmp[i] != tmp[s-1-i]){
      return false;
    }
  }
  return true;
}

int main() {
  memset(tree, 0, sizeof(tree));
  for(long long int i = 1; i <= 10000000; i++) {
    /*if (i == 121) {
      printf("%lld %s, %lld %s\n", i, testpal(i)?"yes":"no", i*i , testpal(i*i)?"yes":"no");
    } else {
      continue;
    }*/
    if (!testpal(i)) continue;
    if (!testpal(i*i)) continue;
    //printf("f: %d\n", i);
    update(i, 1);
  }
  
  int T;
  scanf(" %d", &T);
  for (int t = 0; t < T; t++) {
    long long int a, b;
    scanf(" %lld %lld", &a, &b);
    int root_a = ceil(sqrt((double) a));
    int root_b = floor(sqrt((double) b));
    
    //printf("root_a %d, root_b %d\n", root_a, root_b);
    
    printf("Case #%d: %d\n", t+1, read(root_b) - read(root_a-1));
  }
}
