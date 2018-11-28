// Dom Farolino
// cpuxtech@gmail.com domfarolino@gmail.com
// domfarolino.com

#include <iostream>

using namespace std;

bool arrayIsFull(bool fullNums[]) {
  
  for (int i = 0; i < 10; ++i) {
    if (!fullNums[i]) return false;
  }
  
  return true;
}

void fillOutArray(long N, bool fullNums[]) {
  while (N) {
    fullNums[N%10] = true;
    N /= 10;
  }
}

void printArray(bool fullNums[]) {
  for (int i = 0; i < 10; ++i) {
    cout << fullNums[i] << ", ";
  }
  cout << endl;
}

long lastNumberCounted(long N) {
  if (N <= 0) return -1;
  long max = 1;
  
  bool fullNums[10] = {0};
  long lastNum = 1;

  //TODO: find better optimization after competition
  for (long i = 1; i <= LONG_MAX; ++i) {
    fillOutArray(N*i, fullNums);
    lastNum = N*i;
    if (arrayIsFull(fullNums)) break;
  }

  if (!arrayIsFull(fullNums)) lastNum = -1;
  return lastNum;
}

int main() {
  int T;
  long N;

  cin >> T;
  for (int i = 0; i < T; ++i) {
    cin >> N;
    long lastNumber = lastNumberCounted(N);
    
    if (lastNumber == -1) {
      cout << "Case #" << i+1 << ": INSOMNIA" << endl;
    } else {
      cout << "Case #" << i+1 << ": " << lastNumber << endl;;
    }
  
  }
  
  return 0;
}