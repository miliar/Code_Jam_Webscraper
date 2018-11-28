#include <iostream>
#include <algorithm>
#include <functional>
#include <deque>
#include <cstring>
#include <cstdio>
#include <cstdlib>


using namespace std;

int main()
{
  deque<float> n1,n2,k1,k2;
  float k,n,f;
  int w1,w2;
  int T,N;
  

  cin >> T;
  for (int i = 0; i < T; ++i) {
    printf ("Case #%d: ", i+1);

    n1.clear();
    n2.clear();
    k1.clear();
    k2.clear();
    w1 = w2 = 0;

    cin >> N;
    for (int j = 0; j < N; ++j) {
      cin >> f;
      n1.push_back(f);
      n2.push_back(f);
    }
    for (int j = 0; j < N; ++j) {
      cin >> f;
      k1.push_back(f);
      k2.push_back(f);
    }
    sort (n1.begin(), n1.end());
    sort (n2.begin(), n2.end());
    sort (k1.begin(), k1.end());
    sort (k2.begin(), k2.end());

    for (int j = 0; j < N; ++j) {
      //      for (int kk = 0; kk < N-j; kk++) printf ("n%d: %f, k%d: %f** ", kk,n1[kk], kk,k1[kk]); printf ("\n");
      n = n1[n1.size()-1];
      k = k1[k1.size()-1];
      if (n > k) {
	w1++;
	n1.pop_back();
	k1.pop_back();
      } else {
	n1.pop_front();
	k1.pop_back();
      }
    }
    for (int j = 0; j < N; ++j) {
      //      for (int kk = 0; kk < N-j; kk++) printf ("n%d: %f, k%d: %f** ", kk,n2[kk], kk,k2[kk]); printf ("\n");
      n = n2[n2.size()-1];
      k = k2[k2.size()-1];
      if (n > k) {
	w2++;
	n2.pop_back();
	k2.pop_front();
      } else {
        n2.pop_back();
        k2.pop_back();
      }
    }
    printf ("%d %d", w1, w2);

    printf ("\n");
  }
  
  return 0;
}

