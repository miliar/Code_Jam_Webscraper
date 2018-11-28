#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <functional>
#include <utility>
#include <vector>
#include <list>
#include <queue>
#include <complex>

using namespace std;

typedef list<int> EdgeList;
typedef vector<EdgeList> AdjList;
typedef pair<int, int> ii;
typedef vector<ii> vii;

#define FOR_EDGE(adj,v,it) for (EdgeList::iterator it = adj[v].begin(); \
    it != adj[v].end(); ++it)

struct Point : public complex<double> {
  int idx;
  double& operator[](int idx) {
    if (idx == 0) return complex<double>::real();
    else return complex<double>::imag();
  }
  const double& operator[](int idx) const {
    if (idx == 0) return complex<double>::real();
    else return complex<double>::imag();
  }
};
#define X(p) real(p)
#define Y(p) imag(p)


struct Cmp {
  int idx;
  Cmp(int idx): idx(idx){};
  bool operator()(const Point& p1, const Point& p2) const {
    return p1[idx] < p2[idx];
  }
};

int merge(int* arr, int* arr2, int mid, int n) {
  if (n == 1) {
    *arr2 = *arr;
    return 0;
  }
  int cnt = 0;
  for (int i = 0, left = 0, right = mid; i < n; ++i) {
    if (right >= n) {
      arr2[i] = arr[left++];
    } else if (left == mid) {
      arr2[i] = arr[right++];
    } else if (arr[left] <= arr[right]) {
      arr2[i] = arr[left++];
    } else {
      arr2[i] = arr[right++];
      cnt += mid - left;
    }
  }
  return cnt;
}

int count_inversions(int* arr, int* arr2, int n) {
  int cnt = 0;
  for (int i = 1; i < n; i *= 2) {
    int j;
    for (j = 0; j + i < n; j += 2*i) {
      cnt += merge(arr+j, arr2+j, i, min(2*i, n-j));
    }
    if (j < n) {
      copy(arr + j, arr + n, arr2 + j);
    }
    swap(arr, arr2);
  }
  return cnt;
}

int main() {
  int n_cases;
  scanf("%d", &n_cases);
  int arr[10024];
  int arr2[10024];
  int arr3[10024];
  int arr4[10024];
  int arr5[10024];
  int perm[16];
  for (int ctr = 0; ctr < n_cases; ++ctr) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; ++ i) {
      scanf("%d", &arr[i]);
    }
    printf("Case #%d: ", ctr+1);
    

    int best = 1 << 29;

    for (int i = 0; i < n; ++i) perm[i] = i;
    do {
      for (int i = 0; i < n; ++i) {
        arr2[i] = arr[perm[i]]; 
      }
      
      bool state = 0;
      bool good = true;
      for (int i = 1; i < n; ++i) {
        if (arr2[i] > arr2[i-1]) {
          if (state == 1) {
            good = false;
            break;
          }
        } else {
          if (state == 0) {
            state = 1;
          }
        }
      }

      if (!good) continue;
#ifdef DEBUG
      for (int i = 0; i < n; ++i) {
        printf("%d ", arr2[i]);
      }
      puts("");
#endif

      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
          if (arr[i] == arr2[j]) {
            arr3[i] = j;
            break;
          }
        }
      }


      copy(arr3, arr3+n, arr4);
      int v = count_inversions(arr3, arr4, n);
      best = min(best, v);
      
    } while (next_permutation(perm, perm+n));
    

    printf("%d\n", best);
  }
}
