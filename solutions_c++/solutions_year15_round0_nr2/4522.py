#include <iostream>
#include <cstring>

using namespace std;

typedef struct node {
  int ht[10];
} NODE;


int search(NODE n, int add) {
  if (add >= 9) return 9;
  int max=-1;
  for (int i=9; i>=0; --i) 
    if(n.ht[i]) {
      max = i;
      break;
    }
  if(max <= 1) return 1;
  //if (n.ht[max] >= 2) return max;

  int min_val = max;
  for (int i=1; i<=max/2; ++i) {
    NODE new_n = n;
    new_n.ht[max]--;
    new_n.ht[i]++;
    new_n.ht[max - i]++;
    int search_res = 1 + search(new_n, add + 1);
    if(min_val > search_res) min_val = search_res;
  }
  return min_val;
}

int main() {
  int T, D;
  int P[10];
  cin >> T;
  for (int curT = 1; curT <= T; ++curT) {
    cout << "Case #" << curT << ": ";
    memset(P, 0, sizeof(P));
    cin >> D;
    for (int i=0; i<D; ++i) {
      int tmp;
      cin >> tmp;
      P[tmp]++;
    }
    NODE head;
    for (int i=0; i<10; ++i) 
      head.ht[i] = P[i];
    cout << search(head, 0) << endl;
  }
}
