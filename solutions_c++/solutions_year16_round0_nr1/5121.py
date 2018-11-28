#include <iostream>
using namespace std;

class CountingSheep {
  int digits[10];
  int diCount;
 public:
  CountingSheep():diCount(0) {
    for (int i = 0; i < 10; ++i) {
      digits[i] = 0;
    }
  }
  int getBitNum(int num) {
    int result = 1;
    while (num > 9) {
      result++;
      num /= 10;
    }
    return result;
  }
  int solve(int num) {
    int resultIndex = 0;
    int bit_size = getBitNum(num);
    int size = 10;
    for (int i = 0; i < bit_size; ++i) {
      size *= 10;
    }
    size = std::min(INT_MAX, size);
    for (int i = 1; i < size; ++i) {
      getDigits(num * i);
      if (diCount == 10) {
        resultIndex = i * num;
        return resultIndex;
      }
    }
    return -1;
  }
  void getDigits(int num) {
    while (num > 9) {
      int digit = num % 10;
      if (digits[digit] == 0) {
        diCount++;
        digits[digit] = 1;
      }
      num /= 10;
    }
    if (digits[num] == 0) {
      diCount++;
      digits[num] = 1;
    }
  }
};

int main() {
  int caseNum;
  cin >> caseNum;
  for (int i = 1; i <= caseNum; ++i) {
    int sheep;
    cin >> sheep;
    CountingSheep counter;
    int result = counter.solve(sheep);
    if (result != -1) {
      cout << "Case #" << i << ": " << result << endl;
    } else {
      cout << "Case #" << i << ": " << "INSOMNIA" << endl;
    }
  }
  return 0;
}