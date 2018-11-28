#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;

#define fore(i, l, r) for(int i = l; i < r; i++)
#define forn(i, n) fore(i, 0, n)

typedef vector<int> vi;

int main(){
  int t;
  scanf("%d", &t);
  fore(i, 1, t + 1){
    char arr[1005];
    int n;
    scanf("%d", &n);
    n++;
    scanf("%s", arr);
    vi inp(n);
    forn(j, n){
      inp[j] = arr[j] - '0';
    }
    
    int sum = 0, count = 0;
    forn(j, n){
      if (sum < j){
	count += j - sum;
	sum = j;
      }
      sum += inp[j];
    }
    
    printf("Case #%d: %d\n", i, count);
  }
}
