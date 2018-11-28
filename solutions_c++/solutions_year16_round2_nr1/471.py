#include <bits/stdc++.h>

#define each(i, c) for (auto& i : c)
#define unless(cond) if (!(cond))

using namespace std;

typedef long long int lli;
typedef unsigned long long ull;
typedef complex<double> point;

template<typename P, typename Q>
ostream& operator << (ostream& os, pair<P, Q> p)
{
  os << "(" << p.first << "," << p.second << ")";
  return os;
}

int main(int argc, char *argv[])
{  
  const string D[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

  int tc;
  cin >> tc;
  while (tc--) {
    string s;
    cin >> s;
    map<char, int> cnt;
    for (char c = 'A'; c <= 'Z'; ++c) {
      cnt[c] = count(s.begin(), s.end(), c);
    }
    vector<int> num;
    auto dec = [&] (int n) {
      num.push_back(n);
      each (c, D[n]) --cnt[c];
      return ;
    };    

    while (cnt['Z']) dec(0); // Z -> 0, ZERO
    while (cnt['X']) dec(6); // X -> 6, SIX
    while (cnt['G']) dec(8); // G -> 8, EIGHT
    while (cnt['H']) dec(3); // H -> 3, THREE, EIGHT
    while (cnt['W']) dec(2); // W -> 2, TWO
    while (cnt['U']) dec(4); // U -> 4, FOUR
    while (cnt['S']) dec(7); // S -> 7, SEVEN, SIX
    while (cnt['F']) dec(5); // F -> 5, FIVE, SEVEN
    while (cnt['O']) dec(1); //
    while (cnt['N']) dec(9); //
    
    sort(num.begin(), num.end());
    static int t = 0;
    cout << "Case #" << ++t << ": " << flush;
    each (i, num) cout << i; cout << endl;
  }

  return 0;
}
