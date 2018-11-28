#include <cstdio>
#include <vector>
using namespace std;

#define HUGE 1000000005

vector<int> arr;

void work(int ind) {
  printf("Case #%d: ", ind);
  
  arr.clear();
  int N;
  scanf("%d", &N);
  if(N == HUGE) {
    printf("%d", N);
    return;
  }
  int i;
  int temp;
  for(i = 0; i < N; i++) {
    scanf("%d", &temp);
    arr.push_back(temp);
  }
  int min;
  int minind;
  int j;
  int ans = 0;
  for(i = 0; i < N; i++) {
    min = HUGE;
    minind = -1;
    for(j = 0; j < (int)arr.size(); j++) {
      if(arr[j] < min) {
	min = arr[j];
	minind = j;
      }
    }
    if(minind - 0 < (int)arr.size() - 1 - minind) {
      ans += minind - 0;
    }
    else {
      ans += (int)arr.size() - 1 - minind;
    }
    arr.erase(arr.begin() + minind);
  }
  printf("%d\n", ans);

      
  
}

int main() {
  int T;
  scanf("%d", &T);
  for(int i = 1; i <= T; i++) {
    work(i);
  }
  return 0;
}
