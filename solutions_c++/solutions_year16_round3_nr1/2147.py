#include <iostream>
using namespace std;
int sum_array(int *array, int max) {
  int summ = 0;
  for (int i = 0; i < max; i++)
    summ += array[i];
  return summ;
}
int get_max_index(int *array, int max) {
  int max_val = 0;
  int max_index = -1;
  for (int i = 0; i < max; i++) {
    if (array[i] > max_val) {
      max_index = i;
      max_val = array[i];
    }
  }
  return max_index;
}
int main() {
  int cases;
  cin >> cases;
  for (int i = 0; i < cases; i++) {
    cout << "Case #" << i + 1 << ": ";
    int max = 0;
    int index = -1;
    int nto_max = 0;
    int freq[26];
    int amount;
    cin >> amount;
    for (int z = 0; z < amount; z++) {
      cin >> freq[z];
      if (freq[z] > max) {
        max = freq[z];
        index = z;
      }
    }
    int c = 0;
    while (sum_array(freq, amount) > 0) {
      if(sum_array(freq, amount) == 3) c = 1;

      index = get_max_index(freq, amount);
      char val = index + 'A';
      cout << val;
      freq[index]--;
      c++;
      if (c == 2 ) {
        cout << " ";
        c = 0;
      }
    }
    cout << endl;
  }
  return 0;
}
