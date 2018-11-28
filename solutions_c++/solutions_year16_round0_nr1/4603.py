#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<string>
using namespace std;

int main () {
  long long t;
  string n;
  cin >> t;
  set<char> hasThisDigit;
  for (int i = 0; i < t; i++) {
    hasThisDigit.clear();
    cin >> n;
    long long originalN = atoi(n.c_str());
    if (n == "0") {
      cout << "Case #" << i + 1 << ": INSOMNIA\n";
      continue;
    }
    long long times = 2;
    while (hasThisDigit.size() < 10) {
      for (int j = 0; j < n.size(); j++) {
	//there isn't the digit yet
	if (hasThisDigit.count(n[j]) == 0) {
	  hasThisDigit.insert(n[j]);
	}
	if (hasThisDigit.size() == 10) {
	  cout << "Case #" << i + 1 << ": " << n << endl;
	  break;
	}
      }
      n = to_string(originalN * times);
      times ++;
    }
  }
  return 0;
}