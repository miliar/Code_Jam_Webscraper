#include <iostream>
#include <vector>

using namespace std;

int main(){
  int T;
  freopen("./A-large.in", "r", stdin);
  freopen("./A-large.out", "w+", stdout);
  cin >> T;
  for(int i = 1; i <= T; i++) {
    vector<bool> status (10, false);
    int64_t N;
    cin >> N;
    int64_t cpy = N;
    bool finish = false;
    while(cpy > 0 && !finish) {
      //get all digits
      int64_t tmp = cpy;
      while(tmp != 0) {
        status[tmp % 10] = true;
        tmp /= 10;
      }
      bool result = true;
      for(int j = 0; j < 10 && result; j++) {
        result = result && status[j];
      }
      if (result) {
        finish = true;
        cout << "Case #" << i << ": " << cpy << endl;
      }
      cpy += N;
    }
    if (!finish) {
      cout << "Case #" << i << ": "<< "INSOMNIA" << endl;
    }
  }

}
