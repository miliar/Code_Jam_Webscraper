#include<iostream>
#include<map>
using namespace std;

int main() {
  int tests; cin >> tests;
  for (int t = 1; t <= tests; ++t) {
    string s; cin >> s;
    map<char, int> chars;
    map<int, int> nums;
    for (char c = 'A'; c <= 'Z'; ++c) {
      chars[c] = 0;
    }
    for (string::iterator i = s.begin(); i != s.end(); ++i) {
      chars[*i]++;
    }

    // Count zeroes
    int zeroes = chars['Z'];
    chars['Z'] -= zeroes;
    chars['E'] -= zeroes;
    chars['R'] -= zeroes;
    chars['O'] -= zeroes;
    nums[0] = zeroes;

    // Count eights
    int eights = chars['G'];
    chars['E'] -= eights;
    chars['I'] -= eights;
    chars['G'] -= eights;
    chars['H'] -= eights;
    chars['T'] -= eights;
    nums[8] = eights;

    // Count twos
    int twos = chars['W'];
    chars['T'] -= twos;
    chars['W'] -= twos;
    chars['O'] -= twos;
    nums[2] = twos;

    // Count sixes
    int sixes = chars['X'];
    chars['S'] -= sixes;
    chars['I'] -= sixes;
    chars['X'] -= sixes;
    nums[6] = sixes;

    // Count threes (now that eights are counted)
    int threes = chars['H'];
    chars['T'] -= threes;
    chars['H'] -= threes;
    chars['R'] -= threes;
    chars['E'] -= threes;
    chars['E'] -= threes;
    nums[3] = threes;

    // Count fours
    int fours = chars['U'];
    chars['F'] -= fours;
    chars['O'] -= fours;
    chars['U'] -= fours;
    chars['R'] -= fours;
    nums[4] = fours;
    
    // Count fives (now that fours are counted)
    int fives = chars['F'];
    chars['F'] -= fives;
    chars['I'] -= fives;
    chars['V'] -= fives;
    chars['E'] -= fives;
    nums[5] = fives;

    // Count nines (previous 'i' instances removed)
    int nines = chars['I'];
    chars['N'] -= nines;
    chars['I'] -= nines;
    chars['N'] -= nines;
    chars['E'] -= nines;
    nums[9] = nines;

    // Count sevens (now that fives removed)
    int sevens = chars['V'];
    chars['S'] -= sevens;
    chars['E'] -= sevens;
    chars['V'] -= sevens;
    chars['E'] -= sevens;
    chars['N'] -= sevens;
    nums[7] = sevens;

    // Count ones (last step)
    int ones = chars['O'];
    chars['O'] -= ones;
    chars['N'] -= ones;
    chars['E'] -= ones;
    nums[1] = ones;

    cout << "Case #" << t << ": ";
    for (int i = 0; i < 10; ++i) {
      for (int j = 0; j < nums[i]; ++j) {
	cout << i;
      }
    }
    cout << endl;

  }
}
