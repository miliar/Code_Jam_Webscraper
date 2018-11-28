#include <iostream>
#include <list>
using namespace std;

int main()
{
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    int d;
    cin >> d;
    list<int> plates;
    for (int j = 0; j < d; ++j) {
      int temp;
      cin >> temp;
      plates.push_back(temp);
    }
    int ans = 10000;
    int steps = 0;
    while (true) {
      int max_half = 0;
      int max_whole = 0;
      for (list<int>::iterator it = plates.begin(); it != plates.end(); ++it) {
        max_half = max(max_half, ((*it)+1)/2);
        max_whole = max(max_whole, (*it));
      }
      ans = min(ans, max_whole + steps);
      int max_num = 0;
      for (list<int>::iterator it = plates.begin(); it != plates.end(); ++it) {
        max_num += (((*it)+1)/2 == max_half);
      }
      if (max_half + max_num < max_whole) {
        for (list<int>::iterator it = plates.begin(); it != plates.end(); ++it) {
          if (((*it)+1)/2 == max_half) {
            int val = (*it);
            plates.erase(it);
            plates.push_front(max_half);
            plates.push_front(val - max_half);
          }
        }
        steps += max_num;
      } else {
        steps += max_whole;
        break;
      }
    }
    cout << "Case #" << i+1 << ": " << ans << endl;
  }
}
