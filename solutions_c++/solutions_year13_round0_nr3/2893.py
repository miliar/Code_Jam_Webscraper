#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>

#define MAX 5

bool fair(int num) {

  int size = 0;
  char num_s[MAX];
  
  while(num > 0) {
    num_s[size++] = (num % 10) + '0';
    num /= 10;
  }

  bool fair = true;
  for(int i = 0; i < size / 2; i++)
    if (num_s[i] != num_s[size - i - 1])
      fair = false;

  return fair;
}

bool square_and_fair(int num) {
  double root = sqrt((double) num);
  return (root == floor(root) && fair(root));
}

int main() {

  int tests;
  scanf(" %d", &tests);
  for(int t = 1; t <= tests; t++) {

    int a, b, count = 0;
    scanf(" %d %d", &a, &b);
    for(int i = a; i <= b; i++) {
      if (fair(i) && square_and_fair(i))
	count++;
    } 
    
    printf("Case #%d: %d\n", t, count);
  }

  return 0;
}
