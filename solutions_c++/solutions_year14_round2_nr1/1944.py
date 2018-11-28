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

string reduce(string &s) {
  string t = "";
  t = t + s[0];
  char last = s[0];
  for(size_t i = 1; i < s.size(); i++) {
    if(s[i] != last)
      t = t + s[i];
    last = s[i];
  }
  return(t);
}

bool check(size_t n, vector<string> &words) {
  string s = reduce(*begin(words));
  for(size_t i = 1; i < n; i++)
    if(s != reduce(words[i]))
      return(false);
  return(true);
}

vector<long> rle_encode_one(size_t l, const string &word) {
  vector<long> x(l);
  auto iter = begin(x);
  for(size_t i = 0; i < word.size(); i++) {
    if(i > 0 and word[i] != word[i-1])
      iter++;
    (*iter)++;
  }
  // cerr << word << endl;
  for(auto &y: x)
    cerr << y;
  cerr << endl;
  return(x);
}

vector<vector<long>> rle_encode(size_t l, const vector<string> &words) {
  vector<vector<long>> rle;
  for(auto &w: words)
    rle.push_back(rle_encode_one(l, w));
  return(rle);
}

const size_t LARGE_VAL = 100000000;

long solve(size_t n, vector<string> &words) {
  if(n <= 1)
    return(0);
  if(not check(n, words))
    return(-1);
  else {
    size_t steps = 0;
    string s = reduce(*begin(words));
    size_t l = s.size();
    vector<vector<long>> rle = rle_encode(l, words);

    for(size_t i = 0; i < l; i++) {
      size_t m = 0;
      for(size_t j = 0; j < n; j++)
        if(rle[j][i] > m)
          m = rle[j][i];

      size_t best_step = LARGE_VAL;
      for(long k = 1; k <= m; k++) {
        long step = 0;
        for(size_t j = 0; j < n; j++)
          step += labs(rle[j][i] - k);
        if(step < best_step)
          best_step = step;
      }
      steps += best_step;
    }

    return(steps);
  }
}

int main(int argc, const char **argv)
{
  size_t n;
  cin >> n;

  cerr << "n = " << n << endl;

  for(size_t i = 0; i < n; i++) {
    size_t w;
    cin >> w;

    cerr << "w = " << w << endl;

    vector<string> words(w);
    for(size_t j = 0; j < w; j++)
      cin >> words[j];

    long solution = solve(w, words);

    if(solution < 0)
      cout << "Case #" << (i+1) << ": Fegla Won" << endl;
    else
      cout << "Case #" << (i+1) << ": " << solution << endl;
  }

  return EXIT_SUCCESS;
}

