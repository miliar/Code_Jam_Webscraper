#include <iostream>
#include <string>
#include <vector>

using namespace std;

int countFlips (int arr[], int n) {
  int current_pancake = 0;
  int flips = 0;
  while (current_pancake != n) {
    if (arr[current_pancake] == 1)
      current_pancake++;
    else {
      int flip_end = current_pancake;
      while ((flip_end + 1 < n) &&
	     arr[flip_end + 1] == 0)
	flip_end++;
      if (current_pancake == 0)
	flips++;
      else
	flips += 2;
      current_pancake = flip_end + 1;
    }
  }
  return flips;
}

int main() {
  vector<string> Ni;
  int T;
  cin >> T;
  string s;
  cin.ignore();
  for (int i = 0; i < T; i++) {
    getline(cin, s);
    Ni.push_back(s);
  }
  int count = 1;
  for (auto str : Ni) {
    int arr[100];
    for (int i = 0; i < str.length(); i++) {
      if (str[i] == '+')
	arr[i] = 1;
      else
	arr[i] = 0;
    }
    cout << "Case #" << count++ << ": " << countFlips(arr, str.length()) << endl;
  }
  return 0;
}
