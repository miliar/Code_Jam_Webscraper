#include <iostream>
#include <conio.h>
#include <math.h>
#include <cmath>
#include <cstdlib>
using namespace std;
#if 0
int main() {

  int picknum , num;
  int mask = 0x3ff;
  int sN;
  int i, cnt = 1, last_number = 0, j = 0;
  int num_test = 0;
  cin >> num_test;
  for (j = 0; j < num_test; j++) {

  cin >> picknum;
  mask = 0x3ff;
  cnt = 1;
  while (mask) {
    num = picknum * cnt;
	sN = 1;
	i = 0;
	if (num == 0) {
		cout << "Case #"<<j+1<<": INSOMNIA\n";
		break;
	}
	while (num) {
      num /= 10;
	  sN *= 10;
	}
	sN /= 10;
    num = picknum * cnt;
	while (num) {
		if (num / sN == 0) {
          sN /= 10;
		  continue;
		}
        i = num/sN;
		if (mask & (0x1<<i)) {
          last_number = i;
		}
		mask = mask & ~(0x1<<i);
		
		if (num >= 10 && ((num % sN)*10 < sN)) {
          i = 0;
		  if (mask & (0x1<<i)) {
            last_number = i;
		  }
		  mask = mask & ~(0x1<<i);
		} 
        num = num % sN;
	}
	if (mask == 0) {
		num = picknum*cnt;
		cout << "Case #"<<j+1<<": "<<num<<"\n";
		break;
	}
	++cnt;
  }
  }
  return 0;
}
#endif