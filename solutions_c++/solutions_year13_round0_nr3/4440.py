#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <queue> 
#include <cctype> 
#include <cassert>

using namespace std;

#define VV vector
#define PB push_back
#define SZ(v) ((int)(v).size()) 
#define ll long long
#define ld long double
#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(decltype((b).begin()) a = (b).begin();a!=(b).end();++a)
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi VV<int>
#define vs VV<string>
#define MAX(a,b) ((a)>(b))?((a):(b))
#define MIN(a,b) ((a)<(b))?((a):(b))

#define PROB_ID "C"
#define INPUT_SIZE "small" //"large" //  


bool isFair(ll num) {
  char c1[1000];
  char c2[1000];
  sprintf(c1, "%lld", num);

  int len = strlen(c1);
  int idx = 0;
  for (int j = len - 1; j >= 0; --j) {
    c2[idx++] = c1[j];
  }
  c2[idx] = 0;
  ll num2;
  sscanf(c2, "%lld", &num2);
  if (num == num2) return true;
  return false;
}

int main()
{
	//freopen("my_input.txt", "r", stdin);
	//freopen("my_output.txt", "w", stdout);
	freopen(PROB_ID "-" INPUT_SIZE "-attempt0.in", "r", stdin);
  freopen(PROB_ID "-" INPUT_SIZE "-attempt0.out", "w", stdout);
		
	int T; scanf("%d\n", &T); // remember to put \n

	rep(i, T) {
    ll A, B;
    scanf("%lld%lld\n", &A, &B);
    ll srtA = (ll)sqrt((ld)A);
    ll srtB = (ll)sqrt((ld)B);
    // processing
    // take care of edge cases
    ll startA = srtA - 1;
    while ((startA * startA) < A) startA += 1;
    ll startB = srtB + 2;
    while ((startB * startB) > B) startB -= 1;

    ll counter = 0;
    for (ll j = startA; j <= startB; ++j) {
      if (isFair(j) && isFair(j * j)) {
        counter++;
      }
    }
    // output
		printf("Case #%d: %lld\n", i+1, counter);
	}

	return 0;
}

