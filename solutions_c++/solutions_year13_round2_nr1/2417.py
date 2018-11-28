/*
 * temp.cpp
 *
 *  Created on: Apr 22, 2013
 *      Author: bdai
 */

#include <iostream>
#include <map>
#include <vector>
#include <list>
#include <string>
#include <stack>
#include <queue>
#include <iomanip>
#include <algorithm>
#include <numeric>

#include <stdio.h>
#include <stdint.h>

#define MAX 120

typedef long long Bigint;

using namespace std;


int_fast32_t checkNeed(int start, int target) {
  int step = 0;
  if (start == 1) return 0;
  while(start <= target) {
    start += start - 1;
    step++;
  }
  return step;
}

int_fast64_t addMotes(int start, int target) {
  int_fast64_t ret = 0;
  while (start <= target) {
    ret += start - 1;
    start += start - 1;
  }
  return ret;
}

int main() {
  int T;
  cin >> T;
  for (int_fast32_t t = 1; t <= T; ++t) {
    int_fast64_t A, N;
    cin >> A >> N;
    vector<int_fast64_t> array(N, 0), removed(N + 1, 0), added(N, 0);
    for (int_fast32_t i = 0; i < N; i++)
      cin >> array[i];
    sort(array.begin(), array.end());
    fill(removed.begin(), removed.end(), 0);
    fill(added.begin(), added.end(), 0);

    int prev = 0;
    for (int_fast32_t i = 0; i < N; i++) {
      //cout << i << "@@" << A << ":" << array[i] << endl;
      if (A > array[i]) {
	A += array[i];
      } else {
	int_fast32_t need = checkNeed(A, array[i]);
	//cout << i << "@" << need << endl;
	if (need == 0 || need >= N - i) {
	  prev += N - i;
	  break;
	} else {
	  prev += need;
	  //	  cout << i << "@" << need << ":" << A << " " << addMotes(A, array[i]) << endl;
	  A += addMotes(A, array[i]);
	  A += array[i];
	}
	/*
	if (need > 0)
	  added[i] = prev + need;
	removed[i] = prev + N - i - 1;
	*/
      }
      //prev = added[i];
    }
    //removed[N] = added[N - 1];
    //sort(removed.begin(), removed.end());
    cout << "Case #" << t << ": " << prev << endl;
  }
  return 0;
}
