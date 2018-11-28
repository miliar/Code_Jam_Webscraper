#include <iostream>
#include <climits>

using namespace std;

void update_digits(int num, bool* arr) {
  while (num > 0) {
    arr[num % 10] = true;
    num = num / 10;
  }
}

bool check_digits(const bool* arr) {
  return arr[0]
      && arr[1]
      && arr[2]
      && arr[3]
      && arr[4]
      && arr[5]
      && arr[6]
      && arr[7]
      && arr[8]
      && arr[9];
}

int main() {
  int n;
  cin >> n;

  for (int i = 1; i <= n; i++) {
    int t;
    cin >> t;

    bool bits[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int last_num = 0,
        curr_num;
    bool success = false;
    for (int j = 1; !success; j++) {
      if (INT_MAX / (j+1) < t) break;
      curr_num = j*t;
      if (last_num == curr_num) break;

      update_digits(curr_num, bits);
      success = check_digits(bits);
    }

    cout << "Case #" << i << ": ";
    if (success)
      cout << curr_num << endl;
    else
      cout << "INSOMNIA" << endl;
  }

  return 0;
}
