#include <iostream>
#include <string>

using namespace std;

string pancakes;
int cases = 0, height = 0, flip_count = 0, lowest_blank = -1, lowest_happy = -1;

int get_lowest_blank() {
  for (int i = height - 1; i >= 0; i--) {
    if (pancakes[i] == '-') return i;
  }
  return -1;
}

int get_lowest_happy_from_top() {
  for (int i = 1; i < 100; i++) {
    if (pancakes[i] == '-') return i - 1;
  }
  return -1;
}

int flip_top_n(int n) {
  n = n + 1;
  int half = n / 2;

  for (int i = 0; i < half; i++) {
    char top_flipped = pancakes[i] == '+' ? '-' : '+';
    char bottom_flipped = pancakes[n - 1 - i] == '+' ? '-' : '+';

    pancakes[i] = bottom_flipped;
    pancakes[n - 1 - i] = top_flipped;
  }

  if (n % 2 == 1)
    pancakes[half] = pancakes[half] == '+' ? '-' : '+';
}

int main() {
  cin >> cases;

  for (int n=1; n<=cases; n++) {
    pancakes.clear();
    cin >> pancakes;
    height = pancakes.length();
    flip_count = 0;

    while (true) {
      lowest_blank = get_lowest_blank();

      if (lowest_blank == -1) {
        cout << "Case #" << n << ": " << flip_count << endl;
        break;
      } else if (pancakes[0] == '+') {
        // If top is +, we need to flip top-N + first
        lowest_happy = get_lowest_happy_from_top();
        flip_top_n(lowest_happy);
        flip_count++;
      } else {
        // Top is -, save to flip 1 to lowest_blank
        flip_top_n(lowest_blank);
        flip_count++;
      }
    }
  }

  return 0;
}
