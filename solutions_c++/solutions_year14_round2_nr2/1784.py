/*
 * =====================================================================================
 *
 *       Filename:  solve.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  05/03/2014 05:51:22 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <iostream>

using namespace std;

size_t solve_brute(size_t A, size_t B, size_t k) {
  size_t n = 0;
  for(size_t a = 0; a < A; a++)
    for(size_t b = 0; b < B; b++) {
      // cerr << a << " " << b << " " << (a&b) << " " << k;
      if((a & b) < k) {
        // cerr << " X";
        n++;
      }
      // cerr << endl;
    }
  return(n);
}

int main(int argc, const char **argv)
{
  size_t n;
  cin >> n;

  cerr << "SIZE_MAX = " << SIZE_MAX << endl;
  cerr << "n = " << n << endl;

  for(size_t i = 0; i < n; i++) {
    size_t a, b, k;
    cin >> a >> b >> k;

    cerr << "a = " << a << endl;
    cerr << "b = " << b << endl;
    cerr << "k = " << k << endl;

    auto solution = solve_brute(a, b, k);
    cout << "Case #" << (i+1) << ": " << solution << endl;
  }

  return EXIT_SUCCESS;
}

