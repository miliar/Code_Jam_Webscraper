#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int minus_what;
int appeared[10];

void update(int n) {
  while (n > 0) {
    int e =  n % 10;
    if (!appeared[e]) {
      appeared[e] = 1;
      minus_what -= 1;
    }
    n /= 10;
  }
}

int main() {
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++) {
    int n, m = 0;
    scanf("%d", &n);
    
    minus_what = 10;
    memset(appeared, 0, sizeof(appeared));
   
    int i;
    for (i = 0; i < 1000; i++) {
      update(m); 
      if (!minus_what) break;
      m += n;
    }

    std::ostringstream ss;
    ss << m;

    printf("Case #%d: ", t);
    printf("%s\n", (i == 1000) ? "INSOMNIA" : ss.str().c_str());
  }
  
  return 0;
}
