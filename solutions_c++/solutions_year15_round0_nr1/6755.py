#include <cstdio>
#include <vector>
using namespace std;

int doit(vector<int> & initial) {
  int available = initial[0];
  int needed = 0;
  for (int i = 1; i < initial.size(); ++i) {
    if (initial[i] && available < i) {
      needed += i - available;
      available = i;
    }
    available += initial[i];
  }
  return needed;
}

int main() {
  int nump;
  scanf("%d", &nump);
  for (int i = 0; i < nump; ++i) {
    int numaud;
    scanf("%d", &numaud);
    numaud++;
    char aud[1005];
    scanf("%s", aud);
    vector<int> p;
    for (int j = 0; j < numaud; ++j) {
      p.push_back(aud[j] - '0');
    }
    int result = doit(p);
    printf("Case #%d: %d\n", i+1, result);
  }
  return 0;
}
