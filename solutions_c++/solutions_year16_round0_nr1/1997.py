#include <iostream>
using namespace std;

int main() {
  int t;
  cin >> t;
  for(int i = 0; i < t; i++) {
    long long n, cur, j;
    int left, count;
    bool seen[10];
    cin >> n;

    for(int j = 0; j < 10; j++) seen[j] = false;
    left = 10;
    count = 0;
    cur = 0;
    do {
      cur += n;
      long long copy = cur;
      count++;
      do {
	long long rem = copy%10;
	copy = copy/10;
	if(!seen[rem]) {
	  seen[rem] = true;
	  left--;
	  count = 0;
	}
      } while(copy);
    } while(left != 0 && count != 100);

    cout << "Case #" << (i+1)<< ": ";
    if(left)
      cout << "INSOMNIA" << endl;
    else
      cout << cur << endl;
  }
  return 0;
}
