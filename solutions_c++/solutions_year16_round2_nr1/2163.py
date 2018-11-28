#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;

#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
const int MOD = 1000002013;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

int i, j, k, m, n, l;
int T;

int main()
{
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);


  cin >> T;

  F1(i, T) {
    std::string letters;
    cin >> letters;
    map<char,int> counts;
    vector<char> usedLetters = { 'E', 'F', 'G', 'H', 'I', 'N', 'O', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z' };
    F0(j, usedLetters.size()) {
      counts[usedLetters[j]] = 0;
    }
    F0(j, letters.size()) {
      counts[letters[j]] = counts[letters[j]] + 1;
    }
    vector<char> order = { 'Z', 'G', 'X', 'W', 'H', 'R', 'F', 'V', 'I', 'O' };
    vector<string> words = { "ZERO", "EIGHT", "SIX", "TWO", "THREE", "FOUR", "FIVE", "SEVEN", "NINE", "ONE" };
    vector<int> nums =   { 0, 8, 6, 2, 3, 4, 5, 7, 9, 1 };
    vector<int> numbers = {};
    F0(j, order.size()) {
      int cnt = counts[order[j]];
      F0(k, cnt) {
        numbers.push_back(nums[j]);
        F0(l, words[j].size()) {
          counts[words[j][l]] = counts[words[j][l]] - 1;
        }
      }
    }
    std::sort (numbers.begin(), numbers.end());

    printf("Case #%d: ", i);
    F0(j, numbers.size()) {
      printf("%d", numbers[j]);
    }
    printf("\n");
  }

  return 0;
}
