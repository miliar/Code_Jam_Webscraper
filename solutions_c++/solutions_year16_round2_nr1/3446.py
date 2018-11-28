#include <iostream>
#include <limits>
#include <bitset>
#include <algorithm>
#include <map>

using namespace std;

bool remove(vector<int>& counts, int number) {
  switch (number) {
    case 0:
      if (counts['Z' - 'A'] && counts['E' - 'A'] && counts['R' - 'A'] && counts['O' - 'A']) {
        --counts['Z' - 'A']; --counts['E' - 'A']; --counts['R' - 'A']; --counts['O' - 'A'];
      } else {
        return false;
      }
      break;
    case 1:
      if (counts['O' - 'A'] && counts['N' - 'A'] && counts['E' - 'A']) {
        counts['O' - 'A']--; counts['N' - 'A']--; counts['E' - 'A']--;
      } else {
        return false;
      }
      break;
    case 2:
      if (counts['T' - 'A'] && counts['W' - 'A'] && counts['O' - 'A']) {
        --counts['T' - 'A']; --counts['W' - 'A'];  --counts['O' - 'A'];
      } else {
        return false;
      }
      break;
    case 3:
      if (counts['T' - 'A'] && counts['H' - 'A'] && counts['R' - 'A'] && counts['E' - 'A'] && counts['E' - 'A']) {
        --counts['T' - 'A']; --counts['H' - 'A']; --counts['R' - 'A']; --counts['E' - 'A']; --counts['E' - 'A'];
      } else {
        return false;
      }
      break;
    case 4:
      if (counts['F' - 'A'] && counts['O' - 'A'] && counts['U' - 'A'] && counts['R' - 'A']) {
        --counts['F' - 'A']; --counts['O' - 'A']; --counts['U' - 'A']; --counts['R' - 'A'];
      } else {
        return false;
      }
      break;
    case 5:
      if (counts['F' - 'A'] && counts['I' - 'A'] && counts['V' - 'A'] && counts['E' - 'A']) {
        --counts['F' - 'A']; --counts['I' - 'A']; --counts['V' - 'A']; --counts['E' - 'A'];
      } else {
        return false;
      }
      break;
    case 6:
      if (counts['S' - 'A'] && counts['I' - 'A'] && counts['X' - 'A']) {
        --counts['S' - 'A']; --counts['I' - 'A']; --counts['X' - 'A'];
      } else {
        return false;
      }
      break;
    case 7:
      if (counts['S' - 'A'] && counts['E' - 'A'] && counts['V' - 'A'] && counts['E' - 'A'] && counts['N' - 'A']) {
        --counts['S' - 'A']; --counts['E' - 'A']; --counts['V' - 'A']; --counts['E' - 'A']; --counts['N' - 'A'];
      } else {
        return false;
      }
      break;
    case 8:
      if (counts['E' - 'A'] && counts['I' - 'A'] && counts['G' - 'A'] && counts['H' - 'A'] && counts['T' - 'A']) {
        --counts['E' - 'A']; --counts['I' - 'A']; --counts['G' - 'A']; --counts['H' - 'A']; --counts['T' - 'A'];
      } else {
        return false;
      }
      break;
    case 9:
      if (counts['N' - 'A'] && counts['I' - 'A'] && counts['N' - 'A'] && counts['E' - 'A']) {
        --counts['N' - 'A']; --counts['I' - 'A']; --counts['N' - 'A']; --counts['E' - 'A'];
      } else {
        return false;
      }
      break;
    default:
      cerr << "Uhh Ohh";
      break;
  }
  return true;
}

void add(vector<int>& counts, int number) {
  switch (number) {
    case 0:
      ++counts['Z' - 'A']; ++counts['E' - 'A']; ++counts['R' - 'A']; ++counts['O' - 'A'];
      break;
    case 1:
      counts['O' - 'A']++; counts['N' - 'A']++; counts['E' - 'A']++;
      break;
    case 2:
      ++counts['T' - 'A']; ++counts['W' - 'A'];  ++counts['O' - 'A'];
      break;
    case 3:
      ++counts['T' - 'A']; ++counts['H' - 'A']; ++counts['R' - 'A']; ++counts['E' - 'A']; ++counts['E' - 'A'];
      break;
    case 4:
      ++counts['F' - 'A']; ++counts['O' - 'A']; ++counts['U' - 'A']; ++counts['R' - 'A'];
      break;
    case 5:
      ++counts['F' - 'A']; ++counts['I' - 'A']; ++counts['V' - 'A']; ++counts['E' - 'A'];
      break;
    case 6:
      ++counts['S' - 'A']; ++counts['I' - 'A']; ++counts['X' - 'A'];
      break;
    case 7:
      ++counts['S' - 'A']; ++counts['E' - 'A']; ++counts['V' - 'A']; ++counts['E' - 'A']; ++counts['N' - 'A'];
      break;
    case 8:
      ++counts['E' - 'A']; ++counts['I' - 'A']; ++counts['G' - 'A']; ++counts['H' - 'A']; ++counts['T' - 'A'];
      break;
    case 9:
      ++counts['N' - 'A']; ++counts['I' - 'A']; ++counts['N' - 'A']; ++counts['E' - 'A'];
      break;
    default:
      break;
  }
}

bool find(vector<int>& counts, vector<int>& number) {
  bool stop = true;
  for (auto x : counts) {
    if (x > 0) {
      stop = false;
      break;
    }
  }
  if (stop) {
    return true;
  }

  for (int i = 0; i < 10; ++i) {
    if (remove(counts, i)) {
      number[i]++;
      if (find(counts, number)) {
        return true;
      } else {
        add(counts, i);
        number[i]--;
      }
    }
  }

  return false;
}

int main() {
  std::ios::sync_with_stdio(false);
  int T; cin >> T;
  cin.ignore(numeric_limits<streamsize>::max(), '\n');
  vector<int> counts(26);
  vector<int> number(10);

  for (int i = 1; i <= T; ++i) {
    fill(counts.begin(), counts.end(), 0);
    fill(number.begin(), number.end(), 0);

    string line;
    getline(cin, line);

    for (char c : line) {
      counts[c-'A']++;
    }

    find(counts, number);
    cout << "Case #" << i << ": ";
    for (size_t i = 0; i < number.size(); ++i) {
      while (number[i]-- > 0) {
        cout << i;
      }
    }
    cout << '\n';
  }
}
