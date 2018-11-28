#include<iostream>
#include<fstream>
#include<set>

using namespace std;

set<int> get_digits(int n) {
  set<int> s;
  if (n == 0)
    s.insert(0);
  else {
    while (n > 0) {
      s.insert(n % 10);
      n /= 10;
    }
  }
  return s;
}

int main() {
  
  ifstream fin("A-large.in");
  ofstream fout("A-large.out");

  int T;
  fin >> T;

  for (int t = 1; t <= T; t++) {
    int N;
    fin >> N;
    int last = N;
    
    set<int> s;

    // The maximum number of iterations, 72, was determined by a simple brute force search
    // on all numbers within the limits. It occurs for 125 and multiples of 10 thereof.
    // There is just one "insomnia" case: N = 0.
    for (int n = 1; n <= 72; n++) {
      set<int> next_set = get_digits(n * N);
      for (int i : next_set)
	s.insert(i);
      if (s.size() == 10) {
	last = n * N;
	break;
      }
    }

    if (last == N)
      fout << "Case #" << t << ": INSOMNIA" << endl;
    else
      fout << "Case #" << t << ": " << last << endl;
  }

  return 0;
}
